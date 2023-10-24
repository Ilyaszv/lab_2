from fastapi import FastAPI
import wikipedia
from pydantic import *

app = FastAPI(
    title="Wiki"
)
class searches(BaseModel):
    search_line: str
class num(BaseModel):
    number_of_sent: int = Field(ge=0)

@app.get('/search/{titles}')
def title(titles: str):
    return wikipedia.search(titles)

@app.get('/geodata')
def location(latitude: confloat(ge=-90, le=90), longitude: confloat(ge=-180, le=180)):
    list_loc = wikipedia.geosearch(latitude, longitude)
    dict_images = {}
    for i in range(len(list_loc)):
        dict_images[list_loc[i]] = wikipedia.page(list_loc[i]).images[0]
    return dict_images

@app.post('/')
def get_inf(search_line: searches, number_of_sent: num):
    wikipedia.set_lang("ru")
    return (wikipedia.summary(search_line, sentences=number_of_sent))