from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse


from core.models import ToDo


TODO_URL = reverse("todo-list")
def detail_url(id):
    return reverse("todo-detail",kwargs={"pk":id})


class PublicTestAPI(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_is_private(self):
        res = self.client.get(TODO_URL)
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)


class  PrivateTodosApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user=get_user_model().objects.create_user('test@gmail.com','testpass')
        self.client.force_authenticate(self.user)


    def test_retrieve_todos(self):
        """Retreive all todos """
        res = self.client.get(TODO_URL)
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_create_todo(self):
        """Test post request for creating todo"""
        payload = {
            "title":"Buy groceries",
        }
        res = self.client.post(TODO_URL,payload)
        todo = ToDo.objects.filter(user=self.user).get()
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertEqual(res.data["id"],todo.id)

    def test_partial_update_todo(self):
        """Test updating a Todo with patch"""
        patch={"completed":True}
        todo = ToDo.objects.create(user=self.user,title="Eat")
        url = detail_url(todo.id)
        res = self.client.patch(url,patch,format='json')
        todo.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(todo.completed)
        self.assertEqual(todo.title,res.data.get("title"))


    def test_full_update_todo(self):
        """Test updating a Todo with patch"""
        patch={"title":"Sleep","completed":True}
        todo = ToDo.objects.create(user=self.user,title="make a full update of todo")
        url = detail_url(todo.id)
        res = self.client.patch(url,patch,format='json')
        todo.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(todo.completed)
        self.assertEqual(todo.title,patch.get("title"))


    def  test_delete_Todo(self):
        """Test delete todo """
        todo = ToDo.objects.create(user=self.user,title="test delete ")
        url = detail_url(todo.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code,status.HTTP_204_NO_CONTENT)





