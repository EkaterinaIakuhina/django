from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from students.models import Course
from students.models import Student
from model_bakery import baker


'''making fixtures'''


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make("Course", **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make("Student", **kwargs)
    return factory


'''making tests'''


@pytest.mark.django_db
def test_get_first_course(api_client, course_factory):
    course = course_factory(name='test_course')
    url = reverse('courses-detail', args=[course.id])
    resp = api_client.get(url)

    assert resp.status_code == 200
    assert resp.data['name'] == 'test_course'


@pytest.mark.django_db
def test_get_list_courses(api_client, course_factory):
    courses = [course_factory(name=f'test_course {i}') for i in range(3)]
    url = reverse('courses-list')
    resp = api_client.get(url)

    assert resp.status_code == 200

    created_id = {course.id for course in courses}
    response_id = {course['id'] for course in resp.data}
    assert created_id == response_id
    assert len(created_id) == len(response_id)


@pytest.mark.django_db
def test_filter_by_id(api_client, course_factory):
    course = course_factory(name='test_course')
    url = reverse('courses-list')
    params = {'id': course.id}
    resp = api_client.get(url, params=params)

    assert resp.status_code == 200
    assert resp.data[0]['id'] == course.id


@pytest.mark.django_db
def test_filter_by_name(api_client, course_factory):
    course = course_factory(name='test_course')
    url = reverse('courses-list')
    params = {'name': course.name}
    resp = api_client.get(url, params=params)

    assert resp.status_code == 200
    assert resp.data[0]['name'] == course.name


@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse("courses-list")
    
    name = 'test_course'
    course = {
        'name': name
    }

    resp = api_client.post(url, data=course)
    assert resp.status_code == 201
    assert resp.data['name'] == name


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory(name='test_course')
    url = reverse('courses-detail', args=[course.id])

    new_name = 'new_course'
    new_data = {
        'name': new_name
    }
    resp = api_client.patch(url, new_data)
    assert resp.status_code == 200
    assert resp.data['name'] == new_name


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory(name='test_course')
    url = reverse('courses-detail', args=[course.id])
    resp = api_client.delete(url)
    assert resp.status_code == 204
    assert resp.data is None or len(resp.data) == 0
