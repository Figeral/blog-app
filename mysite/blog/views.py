from django.shortcuts import render,get_object_or_404
from blog.models import post 
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .form import EmailPostForm
from django.core.mail import send_mail

# here the list is been added a paginator 
def post_list(request):
    all=post.objects.all()
    paginate=Paginator(all,3)
    page_number=request.GET.get('page',1)
    try:
       posts=paginate.page(page_number)
    except PageNotAnInteger:
        posts=paginate.page(1)
    except EmptyPage:
      posts=paginate.page(paginate.num_pages) # here in case of empty page, paginate the total number of pages 
                                              #which will return the last page since the ".num_pages" returns a variable 
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts})
    

#creating a second view to display a single post 

def post_detail(request,id):
    try:
        posted=post.objects.get(id=id)
        # paginate=Paginator(host,)
    except post.DoesNotexit:
        raise Http404("NO post found")
    return render(request,
                  "blog/post/detail.html",
                  {"posted":posted}) #here i willfully missed spell the posted to pos
 
#creating a third view for the rendering of all published post   
def postpublish(request):
    collect=post.Published.all()#  adding a page paginator to the post publihed template 
    paginate=Paginator(collect,2)
    page_num=request.GET.get('page',1)
    try:
        post_p=paginate.page(page_num)
    except EmptyPage:
        post_p=paginate.page(1)
    except PageNotAnInteger:
        post_p=paginate.page(paginate.num_pages)
    return render(request,
                  'blog/post/published.html',
                  {'post_p':post_p})


# creating a post_share view which displays form when method is get and handle form when method is post
def post_share(request,post_id):
    posting=get_object_or_404(post,id=post_id)
    
    sent=False
    if request.method=='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(posting.get_absolute_url()) #we retrieve the absolute path of the post using it get_absolute_url
                                                                         #and we use this path as an input for the request.build_absoluste_url() to build
                                                                         #a complete url including the HTTP  schema and hostman
            
            subject=f"{cd['name']} recommends you to read " \
                f"{posting.title}"
            message=f"Read {posting.title} at {post_url}\n\n" \
                f"{cd['name']}\'s comments: {cd['comments']}"
                
            send_mail(subject,message,'mouliofitzgerard@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailPostForm()
    return render(request,'blog/post/share.html',{
           'post':posting,
           'form':form,
           'sent':sent,
        })    
        
