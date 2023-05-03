from sqlalchemy.orm import Session

from .models import Conversation, Message
from .schemas import CreateConversation, ViewConversation, CreateMessage, ViewMessage
from ..authentication.models import User


def create_conversation_crud(db: Session, conversation: CreateConversation):
    created_conversation = Conversation(title=conversation.title)
    db.add(created_conversation)
    db.commit()
    db.refresh(created_conversation)
    for participant in conversation.participants:
        user = db.query(User).filter(User.id == participant).first()
        user.conversations.append(created_conversation)
        db.add(user)
        db.commit()
        db.refresh(user)
    participants = [participant.id for participant in created_conversation.participants]
    return ViewConversation(id=created_conversation.id, title=created_conversation.title,
                            participants=participants, messages=created_conversation.messages)


def create_message_crud(db: Session, message_details: CreateMessage, sender_id: int):
    created_message = Message(content=message_details.content, sender_id=sender_id,
                              receiver_id=message_details.receiver)
    db.add(created_message)
    db.commit()
    db.refresh(created_message)
    return ViewMessage(id=created_message.id, content=created_message.content, sender=created_message.sender_id,
                       receiver=created_message.receiver_id)