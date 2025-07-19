# 📬 Messaging API with Django & DRF

This project is a fully functional **messaging application** backend built using **Django** and **Django REST Framework (DRF)**. It demonstrates the complete lifecycle of building scalable, secure, and RESTful APIs including model design, serialization, viewsets, and nested routing using best practices.
---
## 📌 Features

- ✅ Custom user model with UUIDs and extended fields (phone number, etc.)
- ✅ One-to-many and many-to-many relationships (e.g., conversations ↔ participants, messages ↔ conversations)
- ✅ Nested routing for RESTful endpoints using `drf-nested-routers`
- ✅ DRF viewsets for clean, reusable code
- ✅ API browsable interface & testable via Postman
- ✅ Modular project/app structure

---

## 🧱 Project Structure

messaging_app/
│
├── chats/ # Messaging logic
│ ├── models.py # Models for User, Conversation, Message
│ ├── serializers.py # Serializers with nested relationships
│ ├── views.py # DRF ViewSets
│ ├── urls.py # API routes using DRF Nested Routers
│
├── messaging_app/ # Django project core
│ ├── settings.py
│ ├── urls.py # Project-level routing
│
├── db.sqlite3 # SQLite database
├── manage.py
└── README.md

---

## 🚀 Getting Started

### 🔧 Setup & Run

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
🧩 API Overview
Method	Endpoint	Description
GET	/api/conversations/	List all conversations
POST	/api/conversations/	Create a new conversation
GET	/api/conversations/<id>/messages/	Get all messages in a conversation
POST	/api/conversations/<id>/messages/	Send a message in a conversation

✅ Auth Login (Browsable API)
/api-auth/login/

🧪 Sample Models
CustomUser (Extends AbstractUser)
python
Copy code
user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
phone_number = models.CharField(max_length=15)
Conversation
python
Copy code
conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
participants = models.ManyToManyField(CustomUser, related_name="conversations")
Message
python
Copy code
message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
conversation = models.ForeignKey(Conversation, related_name='messages', ...)
message_body = models.TextField()
sent_at = models.DateTimeField(auto_now_add=True)
📦 Dependencies
Django

Django REST Framework

drf-nested-routers

bash
Copy code
pip install django djangorestframework drf-nested-routers
📁 Example Requests (Postman)
Create a conversation
json
Copy code
POST /api/conversations/
{
  "participants": ["<uuid1>", "<uuid2>"]
}
Send a message
json
Copy code
POST /api/conversations/<conversation_id>/messages/
{
  "sender": "<user_uuid>",
  "message_body": "Hi there!"
}
🧠 Learnings & Concepts
Extending Django’s user model with UUIDs

Modeling one-to-many and many-to-many relationships

Nesting APIs using NestedDefaultRouter

DRF ViewSets and Serializers

