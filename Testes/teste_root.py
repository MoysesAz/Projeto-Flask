from unittest import TestCase, mock
from flask import Flask,url_for
from app import app,render_template
from bs4 import BeautifulSoup
import requests

class Components_in_html(TestCase):

    # Setando configurações de trabalho
    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.app_context = app.test_request_context()
        self.app_context.push()
        self.app.testing = True
        app.config['TESTING'] = True


    def test_home_components(self):
        response = self.client.get(url_for('Home'))
        html = response.get_data(as_text='True')
        soup = BeautifulSoup(html, "html.parser")
        buttons = soup.select("button")
        input = soup.select('input')
        nav = soup.select('nav')
        nav_a = nav[0]
        nav_a = nav_a.select('a')
        self.assertEqual(len(nav_a), 3)
        self.assertEqual(nav_a[0].string, 'Home')
        self.assertEqual(nav_a[1].string, 'Cadastro')
        self.assertEqual(nav_a[2].string, 'Tabela')
        self.assertEqual(len(nav), 1)
        self.assertEqual(len(buttons), 1)
        self.assertEqual(len(input), 2)

    def test_cadastro_components(self):
        response = self.client.get(url_for('Cadastro'))
        html = response.get_data(as_text='True')
        soup = BeautifulSoup(html, "html.parser")
        buttons = soup.select("button")
        input = soup.select('input')
        form = soup.select('form')
        nav = soup.select('nav')
        nav_a = nav[0]
        nav_a = nav_a.select('a')
        self.assertEqual(len(nav_a), 3)
        self.assertEqual(nav_a[0].string, 'Home')
        self.assertEqual(nav_a[1].string, 'Cadastro')
        self.assertEqual(nav_a[2].string, 'Tabela')
        self.assertEqual(len(nav), 1)
        self.assertEqual(len(buttons), 1)
        self.assertEqual(len(input), 4)

    def test_tabela_components(self):
        response = self.client.get(url_for('Tabela'))
        html = response.get_data(as_text='True')
        soup = BeautifulSoup(html, "html.parser")
        nav = soup.select('nav')
        nav_a = nav[0]
        nav_a = nav_a.select('a')
        list_tr = soup.select('tr')
        #self.assertEqual(len(list_tr), QUANTIDADE DE LINES NO BD)
        self.assertEqual(len(nav_a), 3)
        self.assertEqual(nav_a[0].string, 'Home')
        self.assertEqual(nav_a[1].string, 'Cadastro')
        self.assertEqual(nav_a[2].string, 'Tabela')
        self.assertEqual(len(nav), 1)
