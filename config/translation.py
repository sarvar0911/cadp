from modeltranslation.translator import translator, TranslationOptions, register
from cadp_about.models import About, Goal
from cadp_content.models import News, Project, Achievement
from cadp_report.models import Report, Grant

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Goal)
class GoalTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    
    
@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Achievement)
class AchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Report)
class ReportTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Grant)
class GrantTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
