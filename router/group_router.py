from fastapi import APIRouter, Response
from pydantic import BaseModel


router = APIRouter()

groups = set()

state = {"status": 0}


class Group(BaseModel):
    groupId: str


@router.post("/", status_code=201)
async def create(res: Response, group: Group):
    if state["status"] != 0:
        res.status_code = state["status"]
        return res

    if group.groupId in groups:
        res.status_code = 400
        return {"error": "Group already exists"}

    groups.add(group.groupId)
    res.status_code = 201
    return res


@router.delete("/", status_code=200)
async def delete(res: Response, group: Group):
    if state["status"] != 0:
        res.status_code = state["status"]
        return res

    try:
        groups.remove(group.groupId)
    except KeyError:
        pass

    res.status_code = 200
    return res


@router.get("/{groupId}", status_code=200)
async def get(res: Response, groupId: str):
    if state["status"] != 0:
        res.status_code = state["status"]
        return res

    if groupId in groups:
        res.status_code = 200
        return res

    res.status_code = 404
    return {"error": "Group not found"}


@router.get("/", status_code=200)
async def all(res: Response):
    res.status_code = 200
    return [group_id for group_id in groups]


@router.post("/{status_code}", status_code=200)
async def set_state(res: Response, status_code: int):
    state["status"] = status_code
    res.status_code = 200
    return res
