# planning/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import UrbanPlanningRecord
from .forms import UrbanPlanningRecordForm
from .models import Record


def record_list(request):
    records = UrbanPlanningRecord.objects.all()
    return render(request, 'planning/record_list.html', {'records': records})

def record_detail(request, pk):
    record = get_object_or_404(UrbanPlanningRecord, pk=pk)
    return render(request, 'planning/record_detail.html', {'record': record})
def record_new(request):
    if request.method == 'POST':
        form = UrbanPlanningRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = UrbanPlanningRecordForm()
    return render(request, 'planning/record_form.html', {'form': form})

def record_edit(request, pk):
    record = UrbanPlanningRecord.objects.get(pk=pk)
    if request.method == 'POST':
        form = UrbanPlanningRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_detail', pk=record.pk)
    else:
        form = UrbanPlanningRecordForm(instance=record)
    return render(request, 'planning/record_form.html', {'form': form})
def record_delete(request, pk):
    record = get_object_or_404(UrbanPlanningRecord, pk=pk)
    record.delete()
    return redirect('record_list')
def record_search(request):
    query = request.GET.get('q')
    if query:
        records = Record.objects.filter(
            title__icontains=query,
            location__icontains="Murang'a"
        )
    else:
        records = Record.objects.none()
    return render(request, 'planning/record_list.html', {'records': records})