from flask import Flask, redirect, request, make_response, Response
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api

app=Flask(__name__)

