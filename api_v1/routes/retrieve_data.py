from ninja import Router

router = Router(tags=['TEST'])

@router.get('/')
def test_retrieve(request):
  return 200, {'message':"Success"}
