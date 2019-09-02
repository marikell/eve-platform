from api.models.conversations import Conversations
from api.services.generic_service import GenericService
from bson.objectid import ObjectId
from mongoengine.queryset.visitor import Q
import json

class ConversationsService(GenericService):
    def __init__(self):
        super().__init__(Conversations.objects)  
 
    def get_all_by_sender(self, id):
        sender_conversations = Conversations.objects(Q(sender_id=id))
        return sender_conversations

    def delete_by_senderid(self, id):
        senders = self.get_all_by_sender(id)
        for obj in senders:
            sender_id = json.loads(obj.to_json())['_id']['$oid']
            self.delete(sender_id)