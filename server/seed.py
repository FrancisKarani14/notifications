# assuming your app is in app.py and Course model is imported
from app import db, Course
from datetime import datetime

# Drop and create tables (optional, only if you want to reset DB)
db.drop_all()
db.create_all()

courses = [
    Course(
        title="Python for Beginners",
        thumbnail="data:image/png;base64,BASE64_IMAGE_1",
        description="Learn Python from scratch and build projects.",
        duration=5,
        owner="John Doe",
        status="active",
        difficulty="Beginner",
        enrollment_count=150,
        tags="python,programming",
        ratings=4.8,
        review_count=35,
        objectives="Understand Python basics and write simple programs",
        created_at=datetime(2025, 10, 20, 8, 0, 0)
    ),
    Course(
        title="Web Design Basics",
        thumbnail="data:image/png;base64,BASE64_IMAGE_2",
        description="Learn UI/UX design principles and HTML/CSS.",
        duration=4,
        owner="Jane Smith",
        status="active",
        difficulty="Intermediate",
        enrollment_count=200,
        tags="design,frontend",
        ratings=5,
        review_count=42,
        objectives="Design beautiful web pages",
        created_at=datetime(2025, 10, 22, 9, 0, 0)
    ),
    Course(
        title="JavaScript Essentials",
        thumbnail="data:image/png;base64,BASE64_IMAGE_3",
        description="Master the fundamentals of JavaScript programming.",
        duration=6,
        owner="Alice Johnson",
        status="active",
        difficulty="Beginner",
        enrollment_count=180,
        tags="javascript,frontend",
        ratings=4.7,
        review_count=28,
        objectives="Learn JS syntax, DOM manipulation, and events",
        created_at=datetime(2025, 10, 21, 10, 0, 0)
    ),
    Course(
        title="React for Web Development",
        thumbnail="data:image/png;base64,BASE64_IMAGE_4",
        description="Build dynamic web apps using React.js.",
        duration=8,
        owner="Michael Lee",
        status="active",
        difficulty="Intermediate",
        enrollment_count=120,
        tags="react,frontend,web",
        ratings=4.9,
        review_count=50,
        objectives="Understand React components, state, and hooks",
        created_at=datetime(2025, 10, 20, 12, 0, 0)
    ),
    Course(
        title="Node.js & Express",
        thumbnail="data:image/png;base64,BASE64_IMAGE_5",
        description="Create backend servers using Node.js and Express.",
        duration=7,
        owner="Sara Kim",
        status="active",
        difficulty="Intermediate",
        enrollment_count=90,
        tags="nodejs,backend,javascript",
        ratings=4.6,
        review_count=20,
        objectives="Build REST APIs and server-side applications",
        created_at=datetime(2025, 10, 21, 14, 0, 0)
    ),
    Course(
        title="Full-Stack Web Development",
        thumbnail="data:image/png;base64,BASE64_IMAGE_6",
        description="Learn to build full-stack apps with React and Node.js.",
        duration=12,
        owner="David Brown",
        status="active",
        difficulty="Advanced",
        enrollment_count=75,
        tags="fullstack,react,nodejs,web",
        ratings=5,
        review_count=15,
        objectives="Develop complete web applications from frontend to backend",
        created_at=datetime(2025, 10, 22, 15, 0, 0)
    )
]

# Add all courses to the session
db.session.add_all(courses)
db.session.commit()

print("Seeded 6 courses successfully!")
