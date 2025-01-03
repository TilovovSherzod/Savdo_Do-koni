from django.shortcuts import render, get_object_or_404, redirect
from .models import ElektronXizmat, Kategoriya
from .forms import ElektronXizmatForm, XizmatQidiruvForm

def index(request):
    kategoriyalar = Kategoriya.objects.values('id', 'title').distinct()
    xizmatlar = ElektronXizmat.objects.all()
    return render(request, 'index.html', {'kategoriyalar': kategoriyalar, 'xizmatlar': xizmatlar})

def xizmat_royxati(request):
    xizmatlar = ElektronXizmat.objects.all()
    qidiruv_form = XizmatQidiruvForm(request.GET)
    if qidiruv_form.is_valid() and qidiruv_form.cleaned_data.get('qidiruv_sozi'):
        qidiruv_sozi = qidiruv_form.cleaned_data['qidiruv_sozi']
        xizmatlar = xizmatlar.filter(nom__icontains=qidiruv_sozi)
    return render(request, 'xizmatlar.html', {'xizmatlar': xizmatlar, 'qidiruv_form': qidiruv_form})

def xizmat_qoshish(request):
    if request.method == 'POST':
        forma = ElektronXizmatForm(request.POST, request.FILES)
        if forma.is_valid():
            forma.save()
            return redirect('xizmat_royxati')
    else:
        forma = ElektronXizmatForm()
    return render(request, 'xizmat_qoshish.html', {'forma': forma})

def xizmat_tahrirlash(request, pk):
    xizmat = get_object_or_404(ElektronXizmat, pk=pk)
    if request.method == 'POST':
        forma = ElektronXizmatForm(request.POST, request.FILES, instance=xizmat)
        if forma.is_valid():
            forma.save()
            return redirect('xizmat_royxati')
    else:
        forma = ElektronXizmatForm(instance=xizmat)
    return render(request, 'xizmat_tahrirlash.html', {'forma': forma, 'xizmat': xizmat})

def xizmat_ochirish(request, pk):
    xizmat = get_object_or_404(ElektronXizmat, pk=pk)
    if request.method == 'POST':
        xizmat.delete()
        return redirect('xizmat_royxati')
    return render(request, 'xizmat_ochirish.html', {'xizmat': xizmat})
