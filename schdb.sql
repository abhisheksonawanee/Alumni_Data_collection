PRAGMA foreign_keys = ON;

--------------------------------------------------
-- PROGRAMS
--------------------------------------------------
CREATE TABLE IF NOT EXISTS programs (
    program_id      TEXT PRIMARY KEY,
    program_name    TEXT NOT NULL,
    level           TEXT,
    department      TEXT
);

--------------------------------------------------
-- STUDENTS
--------------------------------------------------
CREATE TABLE IF NOT EXISTS students (
    student_id           TEXT PRIMARY KEY,
    program_id           TEXT NOT NULL,
    first_name           TEXT NOT NULL,
    last_name            TEXT NOT NULL,
    email                TEXT NOT NULL UNIQUE,
    entry_term           TEXT,
    grad_term            TEXT,
    status               TEXT,
    citizenship_country  TEXT,
    linkedin_url         TEXT,
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

--------------------------------------------------
-- COURSES
--------------------------------------------------
CREATE TABLE IF NOT EXISTS courses (
    course_id        TEXT PRIMARY KEY,
    course_code      TEXT NOT NULL,
    course_title     TEXT NOT NULL,
    credits          INTEGER,
    level            TEXT,
    home_program_id  TEXT,
    FOREIGN KEY (home_program_id) REFERENCES programs(program_id)
);

--------------------------------------------------
-- FACULTY
--------------------------------------------------
CREATE TABLE IF NOT EXISTS faculty (
    faculty_id   TEXT PRIMARY KEY,
    first_name   TEXT NOT NULL,
    last_name    TEXT NOT NULL,
    email        TEXT UNIQUE,
    title        TEXT,
    department   TEXT
);

--------------------------------------------------
-- COURSE SECTIONS
--------------------------------------------------
CREATE TABLE IF NOT EXISTS course_sections (
    section_id      TEXT PRIMARY KEY,
    course_id       TEXT NOT NULL,
    faculty_id      TEXT NOT NULL,
    term            TEXT,
    year            INTEGER,
    section_number  TEXT,
    modality        TEXT,
    room            TEXT,
    FOREIGN KEY (course_id)  REFERENCES courses(course_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

--------------------------------------------------
-- ENROLLMENTS (Students ↔ Course Sections)
--------------------------------------------------
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id  TEXT PRIMARY KEY,
    section_id     TEXT NOT NULL,
    student_id     TEXT NOT NULL,
    grade          TEXT,
    status         TEXT,
    FOREIGN KEY (section_id) REFERENCES course_sections(section_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

--------------------------------------------------
-- EMPLOYERS
--------------------------------------------------
CREATE TABLE IF NOT EXISTS employers (
    employer_id    TEXT PRIMARY KEY,
    employer_name  TEXT NOT NULL,
    industry       TEXT,
    city           TEXT,
    state          TEXT,
    country        TEXT,
    website        TEXT
);

--------------------------------------------------
-- OPPORTUNITIES
--------------------------------------------------
CREATE TABLE IF NOT EXISTS opportunities (
    opportunity_id   TEXT PRIMARY KEY,
    employer_id      TEXT NOT NULL,
    title            TEXT NOT NULL,
    opportunity_type TEXT,
    location_type    TEXT,
    city             TEXT,
    state            TEXT,
    country          TEXT,
    posted_date      TEXT,
    is_active        INTEGER DEFAULT 1,
    FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
);

--------------------------------------------------
-- STUDENT APPLICATIONS (Students ↔ Opportunities)
--------------------------------------------------
CREATE TABLE IF NOT EXISTS student_applications (
    application_id      TEXT PRIMARY KEY,
    student_id          TEXT NOT NULL,
    opportunity_id      TEXT NOT NULL,
    application_date    TEXT,
    application_status  TEXT,
    FOREIGN KEY (student_id)     REFERENCES students(student_id),
    FOREIGN KEY (opportunity_id) REFERENCES opportunities(opportunity_id)
);

--------------------------------------------------
-- INTERNSHIPS
--------------------------------------------------
CREATE TABLE IF NOT EXISTS internships (
    internship_id          TEXT PRIMARY KEY,
    student_id             TEXT NOT NULL,
    employer_id            TEXT NOT NULL,
    title                  TEXT,
    mode                   TEXT,
    city                   TEXT,
    state                  TEXT,
    country                TEXT,
    start_date             TEXT,
    end_date               TEXT,
    is_related_to_program  INTEGER DEFAULT 0,
    FOREIGN KEY (student_id)  REFERENCES students(student_id),
    FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
);

--------------------------------------------------
-- JOBS (Alumni Outcomes)
--------------------------------------------------
CREATE TABLE IF NOT EXISTS jobs (
    job_id               TEXT PRIMARY KEY,
    student_id           TEXT NOT NULL,
    employer_id          TEXT NOT NULL,
    title                TEXT,
    job_level            TEXT,
    job_type             TEXT,
    employment_status    TEXT,
    city                 TEXT,
    state                TEXT,
    country              TEXT,
    start_date           TEXT,
    end_date             TEXT,
    job_sequence         INTEGER,
    source_internship_id TEXT,
    FOREIGN KEY (student_id)           REFERENCES students(student_id),
    FOREIGN KEY (employer_id)          REFERENCES employers(employer_id),
    FOREIGN KEY (source_internship_id) REFERENCES internships(internship_id)
);

--------------------------------------------------
-- EVENTS
--------------------------------------------------
CREATE TABLE IF NOT EXISTS events (
    event_id       TEXT PRIMARY KEY,
    event_name     TEXT NOT NULL,
    event_type     TEXT,
    event_date     TEXT,
    location       TEXT,
    organizer_unit TEXT
);

--------------------------------------------------
-- EVENT ATTENDANCE (Students ↔ Events)
--------------------------------------------------
CREATE TABLE IF NOT EXISTS event_attendance (
    attendance_id  TEXT PRIMARY KEY,
    event_id       TEXT NOT NULL,
    student_id     TEXT NOT NULL,
    role           TEXT,
    check_in_time  TEXT,
    FOREIGN KEY (event_id)   REFERENCES events(event_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

--------------------------------------------------
-- ORGANIZATIONS (Clubs)
--------------------------------------------------
CREATE TABLE IF NOT EXISTS organizations (
    org_id    TEXT PRIMARY KEY,
    org_name  TEXT NOT NULL,
    org_type  TEXT
);

--------------------------------------------------
-- STUDENT ORGANIZATIONS (Students ↔ Clubs)
--------------------------------------------------
CREATE TABLE IF NOT EXISTS student_organizations (
    student_org_id  TEXT PRIMARY KEY,
    student_id      TEXT NOT NULL,
    org_id          TEXT NOT NULL,
    role            TEXT,
    start_date      TEXT,
    end_date        TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (org_id)     REFERENCES organizations(org_id)
);

--------------------------------------------------
-- SAMPLE DATA
--------------------------------------------------

-- PROGRAMS (sample data)
INSERT INTO programs (program_id, program_name, level, department) VALUES
('MSBA', 'Master of Science in Business Analytics', 'Graduate', 'Eberhardt School of Business'),
('MBA', 'Master of Business Administration', 'Graduate', 'Eberhardt School of Business');

-- STUDENTS (sample data)
INSERT INTO students (student_id, program_id, first_name, last_name, email, entry_term, grad_term, status, citizenship_country, linkedin_url) VALUES
('STU001', 'MSBA', 'Sarah', 'Chen', 'sarah.chen@uop.edu', 'Fall 2023', 'Spring 2025', 'Alumni', 'USA', 'https://linkedin.com/in/sarahchen'),
('STU002', 'MSBA', 'Michael', 'Rodriguez', 'michael.rodriguez@uop.edu', 'Fall 2023', 'Spring 2025', 'Alumni', 'USA', 'https://linkedin.com/in/michaelrodriguez'),
('STU003', 'MBA', 'Emily', 'Johnson', 'emily.johnson@uop.edu', 'Fall 2024', NULL, 'Current', 'USA', 'https://linkedin.com/in/emilyjohnson');

-- FACULTY (sample data)
INSERT INTO faculty (faculty_id, first_name, last_name, email, title, department) VALUES
('FAC001', 'David', 'Thompson', 'david.thompson@uop.edu', 'Professor', 'Eberhardt School of Business'),
('FAC002', 'Lisa', 'Martinez', 'lisa.martinez@uop.edu', 'Associate Professor', 'Eberhardt School of Business');

-- COURSES (sample data)
INSERT INTO courses (course_id, course_code, course_title, credits, level, home_program_id) VALUES
('COURSE001', 'MSBA 201', 'Data Analytics and Visualization', 3, 'Graduate', 'MSBA'),
('COURSE002', 'MSBA 205', 'Machine Learning for Business', 3, 'Graduate', 'MSBA'),
('COURSE003', 'MBA 301', 'Strategic Management', 3, 'Graduate', 'MBA');

-- COURSE SECTIONS (sample data)
INSERT INTO course_sections (section_id, course_id, faculty_id, term, year, section_number, modality, room) VALUES
('SEC001', 'COURSE001', 'FAC001', 'Fall', 2023, '01', 'In-Person', 'ESB 201'),
('SEC002', 'COURSE002', 'FAC001', 'Spring', 2024, '01', 'Hybrid', 'ESB 205'),
('SEC003', 'COURSE001', 'FAC002', 'Fall', 2023, '02', 'In-Person', 'ESB 201'),
('SEC004', 'COURSE003', 'FAC002', 'Fall', 2024, '01', 'In-Person', 'ESB 301');

-- ENROLLMENTS (sample data)
INSERT INTO enrollments (enrollment_id, section_id, student_id, grade, status) VALUES
('ENR001', 'SEC001', 'STU001', 'A', 'Completed'),
('ENR002', 'SEC002', 'STU001', 'A-', 'Completed'),
('ENR003', 'SEC001', 'STU002', 'B+', 'Completed'),
('ENR004', 'SEC002', 'STU002', 'A', 'Completed'),
('ENR005', 'SEC004', 'STU003', 'A', 'Enrolled');

-- EMPLOYERS (sample data)
INSERT INTO employers (employer_id, employer_name, industry, city, state, country, website) VALUES
('EMP001', 'TechCorp Analytics', 'Technology', 'San Francisco', 'CA', 'USA', 'https://techcorp.com'),
('EMP002', 'Global Finance Group', 'Finance', 'New York', 'NY', 'USA', 'https://globalfinance.com');

-- OPPORTUNITIES (sample data)
INSERT INTO opportunities (opportunity_id, employer_id, title, opportunity_type, location_type, city, state, country, posted_date, is_active) VALUES
('OPP001', 'EMP001', 'Data Analyst Intern', 'Internship', 'Hybrid', 'San Francisco', 'CA', 'USA', '2024-01-15', 1),
('OPP002', 'EMP001', 'Business Intelligence Analyst', 'Full-time', 'Remote', 'San Francisco', 'CA', 'USA', '2024-03-01', 1),
('OPP003', 'EMP002', 'Financial Analyst', 'Full-time', 'In-Person', 'New York', 'NY', 'USA', '2024-02-10', 1);

-- STUDENT APPLICATIONS (sample data)
INSERT INTO student_applications (application_id, student_id, opportunity_id, application_date, application_status) VALUES
('APP001', 'STU001', 'OPP001', '2024-01-20', 'Accepted'),
('APP002', 'STU001', 'OPP002', '2024-03-05', 'Interview'),
('APP003', 'STU002', 'OPP001', '2024-01-22', 'Rejected'),
('APP004', 'STU002', 'OPP003', '2024-02-15', 'Accepted');

-- INTERNSHIPS (sample data)
INSERT INTO internships (internship_id, student_id, employer_id, title, mode, city, state, country, start_date, end_date, is_related_to_program) VALUES
('INT001', 'STU001', 'EMP001', 'Data Analyst Intern', 'Hybrid', 'San Francisco', 'CA', 'USA', '2024-06-01', '2024-08-31', 1),
('INT002', 'STU002', 'EMP002', 'Financial Analysis Intern', 'In-Person', 'New York', 'NY', 'USA', '2024-06-15', '2024-09-15', 1);

-- JOBS (sample data)
INSERT INTO jobs (job_id, student_id, employer_id, title, job_level, job_type, employment_status, city, state, country, start_date, end_date, job_sequence, source_internship_id) VALUES
('JOB001', 'STU001', 'EMP001', 'Business Intelligence Analyst', 'Entry-Level', 'Business Analyst', 'Employed', 'San Francisco', 'CA', 'USA', '2024-09-01', NULL, 1, 'INT001'),
('JOB002', 'STU002', 'EMP002', 'Financial Analyst', 'Entry-Level', 'Financial Analyst', 'Employed', 'New York', 'NY', 'USA', '2024-10-01', NULL, 1, NULL);

-- EVENTS (sample data)
INSERT INTO events (event_id, event_name, event_type, event_date, location, organizer_unit) VALUES
('EVT001', 'ESB Career Fair 2024', 'Career Fair', '2024-02-15', 'ESB Building', 'Eberhardt School of Business'),
('EVT002', 'Alumni Networking Night', 'Networking', '2024-04-20', 'ESB Auditorium', 'Eberhardt School of Business');

-- EVENT ATTENDANCE (sample data)
INSERT INTO event_attendance (attendance_id, event_id, student_id, role, check_in_time) VALUES
('ATT001', 'EVT001', 'STU001', 'Attendee', '2024-02-15 10:00:00'),
('ATT002', 'EVT001', 'STU002', 'Attendee', '2024-02-15 10:15:00'),
('ATT003', 'EVT001', 'STU003', 'Attendee', '2024-02-15 10:30:00'),
('ATT004', 'EVT002', 'STU001', 'Attendee', '2024-04-20 18:00:00'),
('ATT005', 'EVT002', 'STU002', 'Attendee', '2024-04-20 18:15:00');

-- ORGANIZATIONS (sample data)
INSERT INTO organizations (org_id, org_name, org_type) VALUES
('ORG001', 'ESB Data Analytics Club', 'Academic Club'),
('ORG002', 'ESB Graduate Student Association', 'Student Government');

-- STUDENT ORGANIZATIONS (sample data)
INSERT INTO student_organizations (student_org_id, student_id, org_id, role, start_date, end_date) VALUES
('STUORG001', 'STU001', 'ORG001', 'President', '2023-09-01', '2024-05-31'),
('STUORG002', 'STU002', 'ORG001', 'Member', '2023-09-01', '2024-05-31'),
('STUORG003', 'STU003', 'ORG002', 'Treasurer', '2024-09-01', NULL);
