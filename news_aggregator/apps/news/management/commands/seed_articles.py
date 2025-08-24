from django.core.management.base import BaseCommand
from django.utils import timezone
from news.models import Article

class Command(BaseCommand):
    help = 'Seed the database with sample articles'

    def handle(self, *args, **kwargs):
        articles = [
            {
                "title": "AI is Revolutionizing Education",
                "content": "Artificial Intelligence is being adopted in schools to enhance personalized learning experiences...",
                "source": "Tech News",
                "published_at": timezone.now(),
                "url": "https://example.com/ai-education"
            },
            {
                "title": "SpaceX Launches New Starlink Satellites", 
                "content": "Today, SpaceX successfully launched another batch of Starlink satellites into orbit...",
                "source": "Space Daily",
                "published_at": timezone.now(),
                "url": "https://example.com/spacex-starlink"
            },
            {
                "title": "Climate Change and Rising Sea Levels",
                "content": "Recent studies show that sea levels are rising faster than previously estimated...",
                "source": "Climate News",
                "published_at": timezone.now(), 
                "url": "https://example.com/climate-change"
            }
        ]

        for article_data in articles:
            article, created = Article.objects.get_or_create(
                title=article_data["title"],
                defaults=article_data
            )
            if created:
                self.stdout.write(f'Created: {article.title}')
            else:
                self.stdout.write(f'Already exists: {article.title}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded articles.'))