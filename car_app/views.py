from django.shortcuts import render, redirect
from .models import CarModel, BrandModel
from django.views.generic import DetailView
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import CommentModel
from .forms import comment_form
from django.utils.decorators import method_decorator
 
    
def home(request , brand_slug=None):
        car = CarModel.objects.select_related('brand').all()
        if brand_slug is not None:
                brand1 = BrandModel.objects.get(slug = brand_slug)
                car = CarModel.objects.filter(brand = brand1)
        brand1 = BrandModel.objects.all()
      
        
        return render(request, 'home.html', {  'data' : car ,  'brand' : brand1})
                
                
                
class detailsView(DetailView):
        model = CarModel
        template_name = 'details.html'
        pk_url_kwarg ='id'
        context_object_name = 'data'
     
        # comment section 
        def post(self, request, *args, **kwargs):
                comment_Form = comment_form(data=self.request.POST)
                car = self.get_object()
                if comment_Form.is_valid():
                        new_comment = comment_Form.save(commit=False)
                        new_comment.car = car
                        new_comment.save()
                return self.get(request, *args, **kwargs)
        
        
        
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                car = self.object
                comments = car.cmt.all()       
                comment_Form = comment_form()           
                context['comments'] = comments
                context['comment_Form'] = comment_Form
                return context


          
class buyView(DetailView):
        model = CarModel
        template_name = 'buy.html'
        pk_url_kwarg ='id'
        context_object_name = 'data1'
        
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                total_quantity = CarModel.objects.aggregate(total=Sum('quantity'))['total']
                context['total_quantity'] = total_quantity
                return context
                        
        
        def post(self, request, *args, **kwargs):
                car = self.get_object()
                if car.quantity > 0:
                        car.quantity -= 1
                        car.save()
                        return redirect('buy')  
                else:
                 return render(request, 'out_of.html')
         
        def success_view(request):
                return render(request, 'buy.html')