from .models import *
from .filters import *
from django.db.models import Q
from django.utils.html import escape
from django.templatetags.static import static
from urllib.parse import urlencode
class SearchToolDataTable:
    def __init__(self, request_params):
        """
        Initialize the service with search parameters.
        """
        columns = [
              'dt_checkbox', 
              'workTitle',
              'workTitleKorean',
              'authorKorean',
              'authorEnglish',
              'translator',
              'sourceTitle',
              'publisher',
              'year',
              'genre',
        ]

        requestOrder = request_params.get("order[0][column]", None)
        if requestOrder and int(requestOrder) == 0:
          requestOrder = 4
        self.orderColumn = None

        if requestOrder:
          orderBy = request_params.get("order[0][dir]")
          self.orderColumn = columns[int(requestOrder)]
          if orderBy == 'desc':
            self.orderColumn = f"-{self.orderColumn}"
        self.keyword = request_params.get("keyword", "")
        self.start = int(request_params.get("start", 0))
        self.length = int(request_params.get("length", 100))
        self.query_params = {
            "authorEnglish2": request_params.get("authorEnglish2", None),
            "authorKorean": request_params.get("authorKorean", None),
            "workTitle": request_params.get("workTitle", None),
            "workTitleKorean": request_params.get("workTitleKorean", None),
            "translator": request_params.get("translator", None),
            "start_date": request_params.get("start_date", None),
            "end_date": request_params.get("end_date", None),
            "year": request_params.get("year", None),
            "sourceTitle": request_params.get("sourceTitle", None),
            "genre": request_params.get("genre", None),
            "publisher": request_params.get("publisher", None),
        }
        self.query_params = {key: value for key, value in self.query_params.items() if value is not None}

    def reponse_data(self):
        total_records, records = self.filter_records()

        data = []
        for record in records:
            record_data =     {
                'dt_checkbox': f'<input type="checkbox" class="record-checkbox" value="{ record.id }">',
                'workTitle': self.check_value_is_nan(record.workTitle),
                'workTitleKorean': self.check_value_is_nan(record.workTitleKorean),
                'authorKorean': self.check_value_is_nan(record.authorKorean),
                'authorEnglish': self.check_value_is_nan(record.authorEnglish),
                'translator': self.check_value_is_nan(record.translator),
                'sourceTitle': self.check_value_is_nan(record.sourceTitle),
                'publisher': self.check_value_is_nan(record.publisher),
                'year': self.check_value_is_nan(record.year),
                'genre': self.check_value_is_nan(record.genre),
                'dt_action_search': self.render_dt_search(record),
            }
            data.append(record_data)
        return total_records, data

    def check_value_is_nan(self, value):
        if value == "nan":
            return None
        else:
            return value

    def render_dt_search(self, record):
        worldcat_url = f"https://worldcat.org/search?q={record.sourceTitle}+{record.publisher}+{record.year}"
        google_url = record.InfoLink if record.InfoLink else f"https://www.google.com/search?tbo=p&tbm=bks&q=intitle:{urlencode({'': record.sourceTitle})[1:]}"
        
        worldcat_icon = static('searchtool/WorldCat Icon33.svg')
        google_icon = static('searchtool/Google icon.svg')

        html = f"""
        <a href="{worldcat_url}" target="_blank">
          <img src="{worldcat_icon}" alt="WorldCat Icon" width="20" height="20" fill="currentColor" class="bi bi-link-45deg" viewBox="0 0 20 20">
        </a>
        <a href="{google_url}" target="_blank">
          <img src="{google_icon}" alt="Google Books Icon" width="18" height="18" fill="currentColor" class="bi bi-link-45deg" viewBox="0 0 18 18">
        </a>
        """
        return html

    def filter_records(self):
        records = Record.objects.all()
        if self.orderColumn:
          records = records.order_by(self.orderColumn)
        authorEnglish2Filter = self.query_params.get("authorEnglish2",None)
        if authorEnglish2Filter:
          authorEnglish2Filter = authorEnglish2Filter.strip()
          authorKorean_arr= records.filter(
            Q(authorEnglish__icontains=authorEnglish2Filter) | 
            Q(authorEnglish2__icontains=authorEnglish2Filter)
          ).values_list('authorKorean', flat=True).distinct()
          records = records.filter(authorKorean__in=authorKorean_arr)
          self.query_params.pop('authorEnglish2', None)
        myFilter = RecordFilter(self.query_params, queryset = records)
        records = myFilter.qs
        if len(self.keyword) > 0:

            filtered_ids = list(records.values_list('id', flat=True))
            search = RecordDocument.search().query(
                "multi_match",
                query=self.keyword,
                fields=[
                    'workTitle', 'workTitleKorean', 'authorKorean',
                    'authorEnglish', 'translator', 'sourceTitle',
                    'publisher', 'year', 'genre'
                ],
                type="cross_fields",
                minimum_should_match="95%"
            ).filter("terms", id=filtered_ids).extra(size=self.length, from_=self.start)

            response = search.execute()
            total_records = response.hits.total['value']
            records = search.to_queryset()
        else:
            total_records = records.count()
            records = records[self.start:self.start + self.length]
        return total_records, records






        # search_filter = Q(name__icontains=self.query) | Q(description__icontains=self.query)

        # # Apply any additional filters
        # for key, value in self.filters.items():
        #     search_filter &= Q(**{key: value})

        # # Perform the search and pagination
        # records = Record.objects.filter(search_filter)
        # total_records = records.count()

        # # Paginate the results
        # start = (self.page - 1) * self.per_page
        # paginated_records = records[start:start + self.per_page]

        # return {
        #     'records': paginated_records,
        #     'total': total_records
        # }
