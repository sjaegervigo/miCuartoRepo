import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows


@app.get("/superheroesDC")
def get_superheroes_dc():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/superheroesMarvel")
def get_superheroes_marvel():
    rows = ["Ironman", "Thor", "Hulk", "Capitan America", "Viuda Negra", "Doctor Strange", "Pantera Negra"]
    return rows


@app.get("/cursosPlatzi")
def get_cursos():
    rows = ["Curso de Python", "Curso de Java", "Curso de JavaScript", "Curso de C++", "Curso de PHP","Curso de Docker"]
    return rows

@app.get("/cursosMicrosoft")
def get_cursos_microsoft():
    rows = ["Curso de Python", "Curso de Java", "Curso de JavaScript", "Curso de C++", "Curso de PHP","Curso de Docker"]
    return rows