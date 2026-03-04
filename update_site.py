import re

# Update index.html
with open('index.html', 'r') as f:
    html_content = f.read()

new_nav_html = '''            <nav class="nav-links">
                <a href="#hero">
                    <i class="fas fa-home"></i>
                    <span>Home</span>
                </a>
                <a href="#">
                    <i class="fas fa-sort-alpha-down"></i>
                    <span>A-Z List</span>
                </a>
                <a href="#">
                    <i class="fas fa-calendar-alt"></i>
                    <span>Schedule</span>
                </a>
            </nav>'''

# Regex to replace the nav-links block
html_content = re.sub(r'<nav class="nav-links">.*?</nav>', new_nav_html, html_content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html_content)

# Update styles.css
with open('styles.css', 'r') as f:
    css_content = f.read()

# Remove old .nav-links a blocks
css_content = re.sub(r'\.nav-links a\s*{[^}]*}', '', css_content)
css_content = re.sub(r'\.nav-links a:hover\s*{[^}]*}', '', css_content)

# Add new styles
new_css = '''
.nav-links a {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    font-weight: 500;
    color: var(--muted-color);
    font-size: 0.8rem;
    transition: all 0.3s ease;
}

.nav-links a i {
    font-size: 1.2rem;
    margin-bottom: 2px;
}

.nav-links a:hover {
    color: white;
    transform: translateY(-2px);
}

.nav-links a:hover i {
    color: var(--accent-color);
}
'''

# Find a good place to insert, e.g., after .nav-links definition
# Or just append, but clean up the old one first (which we did)
# Let's insert it after .nav-links rule to keep organization
insert_pos = css_content.find('.nav-links {')
if insert_pos != -1:
    # Find the closing brace of .nav-links block
    end_brace = css_content.find('}', insert_pos) + 1
    css_content = css_content[:end_brace] + new_css + css_content[end_brace:]
else:
    css_content += new_css

with open('styles.css', 'w') as f:
    f.write(css_content)

print("Files updated successfully")
