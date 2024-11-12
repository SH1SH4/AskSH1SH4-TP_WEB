from django.core.management.base import BaseCommand, CommandError
from main.models import Tag
from random import choice, randint

TAGS = [
    "Python", "JavaScript", "HTML", "CSS", "React", "Node.js", "Django", "Flask", "SQL", "MySQL",
    "PostgreSQL", "MongoDB", "Express", "Angular", "Vue.js", "TypeScript", "C++", "Java", "C#", "Ruby",
    "Rails", "PHP", "Laravel", "Swift", "Kotlin", "Objective-C", "Go", "Rust", "Scala", "R",
    "Machine Learning", "Deep Learning", "Artificial Intelligence", "Data Science", "Data Analysis", "Pandas", "NumPy",
    "SciPy", "TensorFlow", "PyTorch",
    "Keras", "Computer Vision", "NLP", "Natural Language Processing", "API", "REST", "GraphQL", "Docker", "Kubernetes",
    "DevOps",
    "AWS", "Azure", "Google Cloud", "Firebase", "CI/CD", "Git", "GitHub", "GitLab", "Bitbucket", "Agile",
    "Scrum", "Jira", "Trello", "HTML5", "CSS3", "SASS", "LESS", "Bootstrap", "Tailwind CSS", "Web Development",
    "Frontend", "Backend", "Full Stack", "Microservices", "Serverless", "Cybersecurity", "Ethical Hacking",
    "Penetration Testing", "Cryptography", "Encryption",
    "Blockchain", "Bitcoin", "Ethereum", "Smart Contracts", "Solidity", "Web3", "React Native", "Mobile Development",
    "iOS", "Android",
    "Augmented Reality", "Virtual Reality", "Game Development", "Unity", "Unreal Engine", "3D Modeling", "Blender",
    "Graphics", "Design", "UX/UI",
    "Figma", "Adobe XD", "Photoshop", "Illustrator", "SEO", "Content Marketing", "Digital Marketing", "Social Media",
    "Copywriting", "Blogging",
    "E-commerce", "WordPress", "Shopify", "Salesforce", "CRM", "Project Management", "Time Management", "Productivity",
    "Remote Work", "Freelancing",
    "Career Advice", "Interview Preparation", "Resume Writing", "Networking", "Public Speaking", "Leadership",
    "Entrepreneurship", "Startup", "Investment", "Finance",
    "Stock Market", "Personal Finance", "Cryptocurrency", "Trading", "Mathematics", "Statistics", "Algebra", "Calculus",
    "Geometry", "Physics",
    "Chemistry", "Biology", "Astronomy", "History", "Geography", "Philosophy", "Psychology", "Sociology", "Politics",
    "Economics",
    "Law", "Education", "Research", "Writing", "Publishing", "Languages", "Spanish", "French", "German", "Japanese"
]


def create_tag_list(ratio):
    tags = [Tag(title=f'{choice(TAGS)}-{choice(TAGS)}') for _ in
             range(ratio)]
    return tags


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tags = create_tag_list(kwargs['ratio'])
        Tag.objects.bulk_create(tags)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)
