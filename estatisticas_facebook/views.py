from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from estatisticas_facebook.models import Page, PageInsights
import facebook
import json
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

class PageView(TemplateView):
    
    def get_context_data(self, *args, **kwargs):
        context = super(PageView, self).get_context_data(*args, **kwargs)
        return context

def eraseAllPageinsights(request):
    return eraseModelAndReturnHttpResponse(PageInsights)

def eraseAllPages(request):
    return eraseModelAndReturnHttpResponse(Page)

def eraseModelAndReturnHttpResponse(model):
    model.objects.all().delete()
    return HttpResponse("Quantidade de dados na tabela: "+str(model.objects.all().count()))


class PageListView(TemplateView):
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = queryset = Page.objects.filter(name__iexact=slug)
        else:
            queryset = Page.objects.all()
        return queryset
    
    queryset = Page.objects.all()


class PageInsightsListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = PageInsights.objects.filter(
                Q(name__iexact=slug) |
                Q(title__icontains=slug)
            )
        else:
            queryset = PageInsights.objects.all()
        return queryset

class PageInsightsDetailView(DetailView):
    queryset = PageInsights.objects.all()


class PageDetailView(ListView):    
    model = Page
    template_name = "estatisticas_facebook/page_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data( **kwargs)
        pagename = Page.objects.get(pk=self.kwargs['pk'])
  
        token = 'EAACEdEose0cBACo3GqmOSmAiDGDPPmZCHX6N4CBGfWcEuzyZCMBxv6gwi6uSRtwkbuVaXf5bRh53uidkhIcEvuhgGcscagWP0c9XYCYIyXzdKF3iXgpEtYXc5BeWQkZBcLvED3W6hUzv6ZCL0NBFQNu2dZBuD8JxY5z0Leho7W1OZAV9KQ8EjhUWVHfibNfoARIglhu6ZCw9wZDZD'
        graph = facebook.GraphAPI(token)

        raw_json = graph.get_object(pagename.name+'/insights?period=day&metric=page_fan_adds_unique,page_impressions_unique,page_engaged_users,page_stories,page_storytellers&since=2017-01-01')
        pagedata = raw_json['data']

        for obj in pagedata:
            print (obj['name'])
            for value in obj['values']:
                page_insights = PageInsights(
                    name=obj['name'], 
                    period=obj['period'], 
                    title=obj['title'], 
                    description=obj['description'], 
                    end_time=value['end_time'], 
                    value=value['value'], 
                    page_id=self.kwargs['pk'])
                page_insights.save()

        #context['pagedata'] = pagedata


        return context


    
