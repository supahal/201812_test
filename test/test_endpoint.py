import os
import json

import unittest
from nose.tools import assert_equal, assert_true, assert_list_equal, assert_is_not_none, assert_false

from lib.api import get_author, get_book, post_author, post_book, \
    put_author, put_book, delete_author, delete_book, \
    AUTHOR_URL, BOOK_URL
from lib.constants import PROJECT_ROOT


class MethodTest(unittest.TestCase):
    def setUp(self):
        db_file = os.path.join(PROJECT_ROOT, 'data', 'db.json')
        with open(db_file) as fHandle:
            self.data = json.load(fHandle)

    def test_1(self):
        """
        URL format
        :return:
        """
        assert_equal(AUTHOR_URL, 'http://localhost:3000/authors')
        assert_equal(BOOK_URL, 'http://localhost:3000/books')

    def test_2(self):
        """
        GET - author
        :return:
        """
        response = get_author()

        assert_is_not_none(response)
        assert_true(response.ok)
        assert_list_equal(response.json(), self.data['authors'])
        assert_equal(len(response.json()), 5)
        assert_list_equal(list(response.json()[0].keys()), ['id', 'first_name', 'last_name'])

    def test_3(self):
        """
        GET - book
        :return:
        """
        response = get_book()

        assert_is_not_none(response)
        assert_list_equal(response.json(), self.data['books'])
        assert_equal(len(response.json()), 7)
        assert_list_equal(list(response.json()[0].keys()), ['id', 'title', 'author_id', 'copyright'])

    def test_4(self):
        """
        POST - author
        :return:
        """
        stub = {
            "first_name": "Jose",
            "last_name": "Rizal"
        }

        response = post_author(stub)
        assert_is_not_none(response)
        assert_equal(type(response.json()['id']), int)

        response = get_author()
        res = any(dat['id'] == 6 for dat in response.json())
        assert_true(res)

        res = any(dat['first_name'] == "Jose" and dat['last_name'] == "Rizal" for dat in response.json())
        assert_true(res)


    def test_5(self):
        """
        POST - book
        :return:
        """
        stub = {
            "title": "Noli Me Tangere",
            "author_id": 6,
            "copyright": 1887
        }

        response = post_book(stub)
        assert_is_not_none(response)
        assert_equal(type(response.json()['id']), int)

        response = get_book()
        res = any(dat['id'] == 8 for dat in response.json())
        assert_true(res)


        res = any(dat['title'] == "Noli Me Tangere" and dat['author_id'] == 6 and dat['copyright'] == 1887 for dat in response.json())
        assert_true(res)


    def test_6(self):
        """
        PUT - author
        :return:
        """
        stub = {
            "first_name": "Juan",
            "last_name": "Dela Cruz"
        }

        response = put_author(6, stub)

        stub['id'] = 6
        assert_is_not_none(response)
        assert_equal(response.json(), stub)

    def test_7(self):
        """
        PUT - book
        :return:
        """
        stub = {
            "title": "Noli Me Tangere",
            "author_id": 8,
            "copyright": 1889
        }

        response = put_book(8, stub)

        stub['id'] = 8
        assert_is_not_none(response)
        assert_equal(response.json(), stub)

    def test_8(self):
        """
        DELETE - author
        :return:
        """
        response = delete_author(6)
        assert_is_not_none(response)

        # verify if deleted id still in DB
        response = get_author()
        res = any(dat['id'] == 6 for dat in response.json())
        assert_false(res)

    def test_9(self):
        """
        DELETE - book
        :return:
        """
        response = delete_book(8)
        assert_is_not_none(response)

        # verify if deleted id still in DB
        response = get_book()
        res = any(dat['id'] == 8 for dat in response.json())
        assert_false(res)


if __name__ == '__main__':
    unittest.main()
