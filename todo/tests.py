from django.test import TestCase, Client
from django.urls import reverse
import datetime
from todo.models import Tag, Task
from todo.forms import TagForm, TaskForm
from django.contrib.auth.models import User


class ViewsTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            content="Test Task", deadline="2024-03-10 12:00:00"
        )

    def test_task_list_view(self):
        url = reverse("todo:task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_list.html")

    def test_task_create_view(self):
        url = reverse("todo:task-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_update_view(self):
        url = reverse("todo:task-update", kwargs={"pk": self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_delete_view(self):
        url = reverse("todo:task-delete", kwargs={"pk": self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_confirm_delete.html")

    def test_tag_list_view(self):
        url = reverse("todo:tag-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_list.html")

    def test_tag_create_view(self):
        url = reverse("todo:tag-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_form.html")

    def test_tag_update_view(self):
        url = reverse("todo:tag-update", kwargs={"pk": self.tag.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_form.html")

    def test_tag_delete_view(self):
        url = reverse("todo:tag-delete", kwargs={"pk": self.tag.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_confirm_delete.html")

    def test_task_change_status_view(self):
        url = reverse("todo:task_change_status", kwargs={"pk": self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class FormsTest(TestCase):
    def test_tag_form_valid(self):
        form_data = {"name": "Test Tag"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_form_invalid(self):
        form_data = {"name": ""}
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_form_valid(self):
        form_data = {
            "content": "Test Task",
            "deadline": datetime.datetime.now() + datetime.timedelta(days=1),
            "is_done": False,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())


class ModelsTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertTrue(isinstance(tag, Tag))
        self.assertEqual(tag.__str__(), tag.name)

    def test_task_creation(self):
        task = Task.objects.create(content="Test Content",
                                   deadline="2024-03-10 12:00")
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), f"Content: {task.content}")


class AdminTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin",
                                                   password="12345")
        self.client = Client()
        self.client.login(username="admin", password="12345")
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            content="Test Content", deadline="2024-03-10 12:00"
        )

    def test_admin_task_list(self):
        response = self.client.get("/admin/todo/task/")
        self.assertEqual(response.status_code, 200)
