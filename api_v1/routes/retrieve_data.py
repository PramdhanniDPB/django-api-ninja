from ninja import Router

router = Router(tags=['TEST'])

@router.get('/')
def test_retrieve(request):
  return 200, {'message':"Success"}

@router.get('/{id}')
def test_retrieve_by_id(request, id:int):
  return 200, {'id':id,
                'message':'Success'
              }