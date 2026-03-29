import grpc
from protos import item_pb2, item_pb2_grpc
from app.services.item_service import ItemService

class ItemGrpcServicer(item_pb2_grpc.ItemGrpcServiceServicer):
    def GetAllItems(self, request, context):
        # We reuse our exact same fast business logic!
        items = ItemService.get_all_items()
        
        # Map the Pydantic schemas standard Python dicts to Protobuf messages
        proto_items = []
        for item in items:
            proto_items.append(
                item_pb2.ItemResponse(
                    id=item.id,
                    name=item.name,
                    description=item.description or "" # Handle optional fields gracefully
                )
            )
            
        return item_pb2.ItemListResponse(items=proto_items)

    def GetItem(self, request, context):
        item = ItemService.get_item(request.id)
        if not item:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Item with ID {request.id} not found.")
            return item_pb2.ItemResponse()
            
        return item_pb2.ItemResponse(
            id=item.id,
            name=item.name,
            description=item.description or ""
        )
