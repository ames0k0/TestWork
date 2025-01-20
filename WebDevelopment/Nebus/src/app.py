from fastapi import APIRouter, Depends

from . import crud, connections


router = APIRouter()


@router.get('/')
async def get_by_id(
    org_id: int,
    session: Depends(connections.Sqlite.get_scoped_session()),
):
    organization = crud.Organization.get_by_id(
        org_id=org_id,
        session=session,
    )