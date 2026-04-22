# ClinicFlow — Requirements

## 1. Context

ClinicFlow is an appointment-management tool for small medical clinics. It helps clinic staff coordinate who sees which patient when, reduces no-shows through reminders, and gives patients a way to capture basic intake information before they arrive so the visit itself can be more focused.

The system covers three core capabilities: **scheduling appointments**, **sending reminders**, and **collecting basic intake forms**. Billing, insurance, clinical notes, and prescribing are explicitly out of scope — ClinicFlow integrates with or hands off to whatever the clinic already uses for those.

Three roles interact with the system. **Receptionists** run the day-to-day schedule and are the primary power users. **Doctors** consume the schedule and the intake information to prepare for their day. **Patients** book or confirm appointments and fill in intake forms. Because the input spec is thin, several behavioral details (e.g. whether patients self-book or only request, which reminder channels are required) are called out in Section 7.

## 2. User roles

| Role | What they're trying to accomplish |
|------|-----------------------------------|
| Receptionist (REC) | Keep the clinic's daily schedule accurate and full, and make sure patients show up prepared. |
| Doctor (DOC) | Know who they're seeing today, in what order, and what those patients are coming in for. |
| Patient (PAT) | Get an appointment at a convenient time, remember when it is, and show up ready. |

## 3. User stories

### Receptionist

**US-REC-1: Book an appointment for a patient**
As a receptionist,
I want to book an appointment for a patient with a specific doctor at a specific time,
so that the patient is on the schedule and the slot is reserved.

Acceptance criteria:
- Given a doctor has a free slot on a given day and time, when I book that slot for a patient, then the slot is marked occupied and appears on the doctor's schedule.
- Given a doctor already has an appointment at that time, when I try to double-book, then the system blocks the action and shows a clear conflict message.
- Given I book an appointment, when it is saved, then the patient receives a confirmation via their preferred contact channel.

Priority: Must-have

**US-REC-2: Reschedule or cancel an appointment**
As a receptionist,
I want to move or cancel an existing appointment,
so that I can respond to changes without losing track of the patient or the slot.

Acceptance criteria:
- Given an existing appointment, when I change its time to an available slot, then the old slot is freed and the new slot is booked.
- Given an existing appointment, when I cancel it, then the slot becomes available again and the patient is notified.
- Given a rescheduled or cancelled appointment, when the change is saved, then the change is reflected on the doctor's schedule immediately.

Priority: Must-have

**US-REC-3: See today's full schedule at a glance**
As a receptionist,
I want a single view of every appointment across all doctors for the current day,
so that I can answer walk-in and phone questions without clicking through each doctor's calendar.

Acceptance criteria:
- Given it is a given day, when I open the day view, then I see every appointment for every doctor in that clinic, with patient name and appointment type.
- Given a patient arrives, when I mark them as checked in, then their appointment is visibly flagged as arrived.

Priority: Must-have

**US-REC-4: Find a patient's upcoming appointment quickly**
As a receptionist,
I want to search for a patient by name or phone number,
so that I can locate or update their appointment without scrolling the schedule.

Acceptance criteria:
- Given a patient exists in the system, when I search any substring of their name or phone number, then matching patients appear within the search results.
- Given I select a patient, when the patient has upcoming appointments, then I see those appointments with dates, times, and assigned doctor.

Priority: Should-have

**US-REC-5: See which patients have not completed intake**
As a receptionist,
I want a view of upcoming appointments flagged with intake-form status,
so that I can nudge patients who haven't filled theirs in before they arrive.

Acceptance criteria:
- Given a patient has an appointment within N days, when intake is incomplete, then that appointment shows an "intake pending" indicator.
- Given I select an appointment with pending intake, when I trigger a reminder, then the patient is re-sent the intake link.

Priority: Should-have

### Doctor

**US-DOC-1: See my day's schedule**
As a doctor,
I want to see my appointments for today in chronological order,
so that I know who I'm seeing and when.

Acceptance criteria:
- Given I am logged in, when I open my day view, then I see my appointments for today with patient name, time, duration, and appointment reason.
- Given an appointment is cancelled or rescheduled, when I refresh my view, then the change is reflected without needing to restart.

Priority: Must-have

**US-DOC-2: Review a patient's intake form before the visit**
As a doctor,
I want to read the intake responses a patient submitted,
so that I can walk into the room already knowing the basics of why they're here.

Acceptance criteria:
- Given a patient has submitted their intake form, when I open their appointment, then I see their responses clearly laid out.
- Given a patient has not submitted intake, when I open their appointment, then the system tells me intake is missing.

Priority: Must-have

**US-DOC-3: See my schedule for an upcoming day**
As a doctor,
I want to view my schedule for any future day within the clinic's booking horizon,
so that I can plan around meetings, time off, or heavy days.

Acceptance criteria:
- Given a future date within the booking horizon, when I navigate to it, then I see my appointments for that day.
- Given a day I've marked as unavailable, when I view it, then the day is clearly marked as blocked.

Priority: Should-have

**US-DOC-4: Block off time when I'm unavailable**
As a doctor,
I want to mark blocks of time as unavailable (e.g. admin time, lunch, time off),
so that reception and patients don't book me into those slots.

Acceptance criteria:
- Given I mark a time block as unavailable, when reception or a patient views my availability, then the block is not bookable.
- Given I already have appointments in a time range, when I try to block that range, then the system warns me and lists the conflicting appointments before confirming.

Priority: Should-have

### Patient

**US-PAT-1: Request or book an appointment**
As a patient,
I want to get an appointment at a time that works for me,
so that I can be seen without a long phone back-and-forth.

Acceptance criteria:
- Given I choose a doctor and a visit reason, when I pick an available time, then an appointment is created (or a request is submitted — see Open questions).
- Given I submit the booking, when it is confirmed, then I receive a confirmation with date, time, doctor, and location.

Priority: Must-have

**US-PAT-2: Receive reminders before my appointment**
As a patient,
I want reminders ahead of my appointment,
so that I don't forget or miss it.

Acceptance criteria:
- Given I have an upcoming appointment, when the reminder window starts, then I receive a reminder via my preferred channel.
- Given I receive a reminder, when I click/tap it, then I can see the appointment details and a link to my intake form if it's still pending.

Priority: Must-have

**US-PAT-3: Fill in an intake form before arriving**
As a patient,
I want to answer basic intake questions from home,
so that my appointment isn't spent filling out paper forms in the waiting room.

Acceptance criteria:
- Given I have a pending intake for an upcoming appointment, when I open the intake link, then I see the clinic's intake questions and can complete them.
- Given I submit the intake, when it is saved, then I can no longer be told I'm "missing" intake for that appointment.

Priority: Must-have

**US-PAT-4: Reschedule or cancel my own appointment**
As a patient,
I want to move or cancel my own appointment within a reasonable window,
so that I don't have to call the clinic for minor changes.

Acceptance criteria:
- Given I have an upcoming appointment outside the clinic's lock-in window, when I choose to cancel, then the slot is released and I get a cancellation confirmation.
- Given I have an upcoming appointment, when I choose to reschedule, then I can pick a new available slot with the same doctor.
- Given I try to change an appointment inside the lock-in window (e.g. <24h), when I attempt it, then the system tells me to contact the clinic.

Priority: Should-have

## 4. User journeys

**UJ-REC-1: Managing a day at the front desk**
Role: Receptionist
Trigger: Start of the clinic day
Outcome: Every patient for the day is seen, checked-in, and any schedule changes are reflected cleanly.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Open day | Opens today's schedule view | Shows all appointments across doctors, with check-in and intake status | Wants one screen, not six; anxious if info is scattered |
| 2. Triage | Scans which patients have incomplete intake | Flags each row with intake status | Annoyed at chasing the same patients repeatedly |
| 3. Handle walk-ins and changes | Books, reschedules, or cancels as needed | Validates slot availability, notifies patient and doctor | Pressured by phone + front-desk traffic at once |
| 4. Check patients in | Marks arrivals as they happen | Updates doctor's view in real time | Feels productive when changes land instantly |
| 5. Wrap up | Reviews unfilled or no-show slots | Shows day summary of completed / no-show / cancelled | Frustrated by no-shows, wants better reminders next time |

Supporting stories: US-REC-1, US-REC-2, US-REC-3, US-REC-4, US-REC-5

**UJ-DOC-1: Preparing for and running a clinic day**
Role: Doctor
Trigger: Morning of clinic day
Outcome: Doctor sees every scheduled patient prepared, without having to chase information.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Preview | Opens today's schedule | Lists appointments in order, with reason and intake status | Curious — what am I walking into today? |
| 2. Prep per patient | Opens the next patient's intake | Shows submitted responses; flags if missing | Frustrated when intake is empty and unprepared |
| 3. Adjust | Blocks out a slot after a cancellation or to catch up | Marks slot unavailable and frees it from booking | Relieved to have breathing room |
| 4. Plan ahead | Checks upcoming days for heavy loads | Shows future days with load indicators | Mild dread if tomorrow looks packed |

Supporting stories: US-DOC-1, US-DOC-2, US-DOC-3, US-DOC-4

**UJ-PAT-1: Getting seen at the clinic**
Role: Patient
Trigger: Health concern or routine need
Outcome: Patient attends a confirmed appointment, prepared, without missing or forgetting it.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Discover | Opens clinic's booking page | Shows available doctors and times | Unsure which doctor or slot fits |
| 2. Book | Chooses a slot and submits | Confirms (or forwards to reception) and sends confirmation | Relieved; mildly anxious if confirmation is delayed |
| 3. Prepare | Receives intake-form link | Presents questions, saves responses | Mildly annoyed by form length; relieved to do it at home |
| 4. Remember | Receives reminder(s) | Sends reminder with details and intake link if pending | Grateful for the nudge |
| 5. Adjust (if needed) | Reschedules or cancels | Releases old slot, confirms new one | Frustrated if lock-in window blocks a genuine need |
| 6. Attend | Arrives for appointment | Marks them checked in (via reception) | Calm — no surprises at the desk |

Supporting stories: US-PAT-1, US-PAT-2, US-PAT-3, US-PAT-4

## 5. Features

### Core scheduling

**F-1: Appointment calendar**
Description: A shared calendar showing all doctors' appointments, supporting per-doctor and all-doctor views for any day within the booking horizon.
Supports stories: US-REC-1, US-REC-2, US-REC-3, US-DOC-1, US-DOC-3
Supports journeys: UJ-REC-1, UJ-DOC-1
Priority: Must-have
Notes: Must reflect updates without manual refresh where possible.

**F-2: Booking and conflict prevention**
Description: Logic to create, move, and cancel appointments while enforcing that a doctor is never double-booked and that a slot can't be booked during a block-off.
Supports stories: US-REC-1, US-REC-2, US-PAT-1, US-PAT-4, US-DOC-4
Supports journeys: UJ-REC-1, UJ-PAT-1, UJ-DOC-1
Priority: Must-have
Notes: Open question — is patient booking direct or request-and-confirm? See Section 7.

**F-3: Doctor availability and block-offs**
Description: Lets doctors mark themselves unavailable for a time range (lunch, admin, time off) and enforces those blocks at booking time.
Supports stories: US-DOC-4
Supports journeys: UJ-DOC-1, UJ-REC-1
Priority: Should-have

**F-4: Patient record / directory**
Description: A minimal patient record (name, contact info, preferred reminder channel) that appointments and intake forms attach to, and that reception can search.
Supports stories: US-REC-1, US-REC-4, US-PAT-1, US-PAT-2
Supports journeys: UJ-REC-1, UJ-PAT-1
Priority: Must-have
Notes: Explicitly minimal — no clinical history, no billing data.

**F-5: Check-in tracking**
Description: Lets reception mark a patient as arrived, visible to the assigned doctor in real time.
Supports stories: US-REC-3, US-DOC-1
Supports journeys: UJ-REC-1, UJ-DOC-1
Priority: Should-have

### Reminders and notifications

**F-6: Appointment confirmations**
Description: Sends a confirmation message to the patient whenever an appointment is booked, rescheduled, or cancelled.
Supports stories: US-REC-1, US-REC-2, US-PAT-1, US-PAT-4
Supports journeys: UJ-PAT-1, UJ-REC-1
Priority: Must-have
Notes: Channel (SMS, email, both) is an open question — see Section 7.

**F-7: Appointment reminders**
Description: Sends one or more automated reminders to patients ahead of their appointment, with a link back to appointment details and intake if pending.
Supports stories: US-PAT-2, US-REC-5
Supports journeys: UJ-PAT-1, UJ-REC-1
Priority: Must-have
Notes: Timing cadence (e.g. 24h + 1h) is an open question.

### Intake forms

**F-8: Intake form delivery and completion**
Description: Sends patients a link to a clinic-defined intake form after booking and lets them complete it from any device.
Supports stories: US-PAT-3, US-REC-5
Supports journeys: UJ-PAT-1, UJ-REC-1
Priority: Must-have

**F-9: Intake responses for doctors**
Description: Surfaces submitted intake responses to the assigned doctor on the appointment view, and clearly flags when intake is missing.
Supports stories: US-DOC-2, US-REC-5
Supports journeys: UJ-DOC-1, UJ-REC-1
Priority: Must-have
Notes: Depends on F-8.

**F-10: Intake nudges for reception**
Description: A list / filter of upcoming appointments whose intake is still pending, with a one-click action to resend the intake link.
Supports stories: US-REC-5
Supports journeys: UJ-REC-1
Priority: Should-have

### Access and roles

**F-11: Role-based access**
Description: Separate access levels for receptionists, doctors, and patients, with each seeing only what's appropriate (doctors see their own schedule and their patients' intake; patients see only their own data).
Supports stories: US-REC-1, US-REC-2, US-REC-3, US-DOC-1, US-DOC-2, US-PAT-1, US-PAT-3
Supports journeys: UJ-REC-1, UJ-DOC-1, UJ-PAT-1
Priority: Must-have
Notes: Specific auth mechanism (magic link, password, clinic SSO) not specified — see Section 7.

## 6. Traceability matrix

| Story | Feature(s) | Journey(s) |
|-------|------------|------------|
| US-REC-1 | F-1, F-2, F-4, F-6, F-11 | UJ-REC-1 |
| US-REC-2 | F-1, F-2, F-6, F-11 | UJ-REC-1 |
| US-REC-3 | F-1, F-5, F-11 | UJ-REC-1 |
| US-REC-4 | F-4 | UJ-REC-1 |
| US-REC-5 | F-7, F-9, F-10 | UJ-REC-1 |
| US-DOC-1 | F-1, F-5, F-11 | UJ-DOC-1 |
| US-DOC-2 | F-9, F-11 | UJ-DOC-1 |
| US-DOC-3 | F-1 | UJ-DOC-1 |
| US-DOC-4 | F-2, F-3 | UJ-DOC-1, UJ-REC-1 |
| US-PAT-1 | F-2, F-4, F-6, F-11 | UJ-PAT-1 |
| US-PAT-2 | F-4, F-7 | UJ-PAT-1 |
| US-PAT-3 | F-8, F-11 | UJ-PAT-1 |
| US-PAT-4 | F-2, F-6 | UJ-PAT-1 |

Every story maps to at least one feature and one journey; every journey is supported by stories from its primary role.

## 7. Open questions

1. **Patient self-booking vs. request-and-confirm.** The spec says "scheduling appointments" but doesn't say whether patients book directly into open slots or submit requests that reception confirms. This changes F-2 and UJ-PAT-1 meaningfully. Assumption pending clarification: patients can self-book into open slots, with reception able to override.
2. **Reminder channels.** "Reminders" is listed in scope but not whether SMS, email, push, or all of the above are required. Assumption pending clarification: email at minimum, SMS if the clinic provides a sending number. Needed for F-6 and F-7.
3. **Reminder cadence.** How many reminders, and how far before the appointment? Common pattern is 24h + 1h, but the spec doesn't say. Needed for F-7.
4. **Intake form authoring.** Are intake questions fixed for all clinics, per-clinic configurable, or per-appointment-type? This affects F-8 substantially.
5. **Cancellation / reschedule lock-in window.** US-PAT-4 assumes a window (e.g. <24h) during which patients can't self-cancel, but this isn't in the spec.
6. **Multi-clinic vs single-clinic.** Is ClinicFlow installed per clinic, or is it a multi-tenant product where one receptionist might handle multiple clinics? Assumption: single clinic per deployment.
7. **Authentication.** How do doctors and patients sign in? Passwords, magic links, SSO? Relevant to F-11.
8. **Admin role.** Who configures doctors, clinic hours, intake questions, and reminder settings? No admin role was listed; either receptionists double as admins or a role is missing.
9. **No-show handling.** Should the system automatically flag no-shows, charge fees, or just record them? Billing is out of scope, so fees are out, but recording/flagging may still be wanted.
10. **Data residency / privacy constraints.** Medical context usually implies HIPAA or equivalent regulatory requirements. The spec doesn't mention them; they would shape F-4, F-8, and F-11.
