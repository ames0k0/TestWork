import csv
import asyncio
from pathlib import Path

from aiohttp import web


async def create_file(file: Path):
    fieldnames = ("Файл", "Ссылка")
    data = [
        {fieldnames[0]: i, fieldnames[1]: j} for i, j in \
        (
            ("Курс золота",
             "http://0.0.0.0:8080/data_gold/"),
            ("Динамика индекса Золото",
             "http://0.0.0.0:8080/data_gold_dynamic_index/"
            ),
            ("Курс золота за 3 мес.",
             "http://0.0.0.0:8080/data_gold/3"
            ),
            ("Динамика индекса Золото за 3 мес.",
             "http://0.0.0.0:8080/data_gold_dynamic_index/3"
            ),
            ("Курс золота за 5 мес.",
             "http://0.0.0.0:8080/data_gold/5"
            ),
            ("Динамика индекса Золото за 5 мес.",
             "http://0.0.0.0:8080/data_gold_dynamic_index/5"
            ),
            ("Курс золота за 10 мес.",
             "http://0.0.0.0:8080/data_gold/10"
            ),
            ("Динамика индекса Золото за 10 мес.",
             "http://0.0.0.0:8080/data_gold_dynamic_index/10"
            )
        )
    ]
    with open(file, "w", newline="") as ftw:
        writer = csv.DictWriter(ftw, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


async def csv_file(_):
    file = Path("gold-fi-data.csv")
    if not file.exists():
        await create_file(file)
    return web.FileResponse(file)


async def data_gold(request):
    delay = request.match_info.get('delay')
    if delay:
        await asyncio.sleep(int(delay))
    return web.Response(
        text="""
        <table class="gold-by-date">
            <thead>
                <tr>
                    <th>Дата</th>
                    <th>Значение</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>25.09.2024</tb>
                    <td>7 851.94</tb>
                </tr>
                <tr>
                    <td>24.09.2024</tb>
                    <td>7 784.83</tb>
                </tr>
                <tr>
                    <td>23.09.2024</tb>
                    <td>7 665.96</tb>
                </tr>
            </tbody>
        </table>
        """,
        content_type="text/html"
    )


async def data_gold_dynamic_index(request):
    delay = request.match_info.get('delay')
    if delay:
        await asyncio.sleep(int(delay))
    return web.Response(
        text="""
        <table class="gold-by-dynamic-index">
            <tr>
                <th>Период</th>
                <th>Проценты</th>
            </tr>
            <tr>
                <td>3 месяца</td>
                <td>19.72</td>
            </tr>
            <tr>
                <td>1 год</td>
                <td>33.29</td>
            </tr>
            <tr>
                <td>3 года</td>
                <td>91.79</td>
            </tr>
        </table>
        """
    )


async def init_app():
    app = web.Application()
    app.add_routes([web.get('/', csv_file)])
    app.add_routes([web.get('/data_gold/{delay}', data_gold)])
    app.add_routes([web.get('/data_gold_dynamic_index/{delay}', data_gold_dynamic_index)])
    return app


if __name__ == "__main__":
    web.run_app(init_app())
