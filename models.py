from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from datetime import timedelta

class Event(models.Model):
    LIGHT = 'dj_timetable_light'
    DARK = 'dj_timetable_dark'

    THEME_CHOICES = [
        (LIGHT, 'Light'),
        (DARK, 'Dark'),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="Event Name")
    start_date = models.DateField(help_text="Date when the Event is schedule for.", verbose_name="Event Date")
    theme_color = models.CharField(max_length=20, choices=THEME_CHOICES, default=LIGHT, verbose_name="Theme Color", help_text="How the event section will look when display on any page")
    
    def generate_shortcode(self):
        """Generate a shortcode for template inclusion tag."""
        return f'{{% display_event "{self.name}" %}}'

    def __str__(self):
        return self.name
class TimeTable(models.Model):
    item_event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='items', verbose_name="Event Name")
    start_time = models.TimeField(verbose_name="Start Time", help_text="When this will start")
    end_time = models.TimeField(verbose_name="End Time", help_text="When this will end", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    title =models.CharField(max_length=70, verbose_name="Item Title", help_text="Event item title.")
    description = models.TextField(verbose_name="Item Description", help_text="Event item description.", blank=True, null=True)

    def __str__(self):
        return f"{self.start_time} - {self.description}"
    class Meta:
        ordering = ['start_time']