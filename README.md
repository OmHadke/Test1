# Test1
DAA Proj

## Restaurant Management System (RMS) Roadmap

This project will be delivered in phases so the MVP is stable before adding AI and analytics.

### Phase 1: MVP (Exam-safe)

**Core roles**
- Restaurant Admin
- Customer
- System Admin (optional later)

**Restaurant registration**
- Capture restaurant name, address/location, contact details, opening hours, and login credentials.
- Generate a unique restaurant ID and a QR code that links to:
  - `https://yourapp.com/menu/{restaurantId}`

**Menu & dish management**
- Dishes include: name, image (required), ingredients, cooking methodology, calories, category, recommended-for tags, price, availability.
- Store images in Cloudinary or AWS S3.

**Customer flow (QR-based)**
- Scan QR → open menu → view dish details → add to cart → place order/pre-order.
- Login only required for booking, reviews, or payment.

**Customer registration**
- Name, email/phone, food preference, allergies (optional).

**Table booking (basic)**
- Restaurant sets table count and seats per table.
- Customer selects date/time/party size.
- System checks availability and confirms booking.

**Payment (simple)**
- Start with COD/pay at restaurant or Razorpay.

**Reviews & ratings**
- Rating (1–5) and comment after orders.

### Phase 2: AI Feature (Single, focused)
- Add food image recognition using a pre-trained CNN (e.g., MobileNet/ResNet).
- If not recognized, show similar dishes.
- Train on a small dataset (20–30 dishes).

### Phase 3: Analytics (High-ROI)
- Most ordered dish
- Peak hours
- Average rating
- Revenue per day
- Visualize with Chart.js or Recharts

## Recommended Stack

**Frontend**: React, Tailwind CSS, `html5-qrcode`

**Backend**: Node.js, Express, JWT auth

**Database**: MongoDB

**Image storage**: Cloudinary

## Minimal Data Model

**Restaurant**
```json
{
  "_id": "restaurantId",
  "name": "",
  "location": "",
  "menu": ["dishId"],
  "qrCode": ""
}
```

**Dish**
```json
{
  "name": "",
  "image": "",
  "ingredients": [],
  "calories": 250,
  "recommendedFor": ["diabetic", "fitness"]
}
```

**User**
```json
{
  "name": "",
  "email": "",
  "preferences": []
}
```

## Mobile App Prototype

A starter Expo (React Native) app is available under `mobile-app/` with screens that map to the RMS MVP: restaurant registration, menu highlights, booking slots, and review snapshot.

### Run locally

```bash
cd mobile-app
npm install
npm run start
```
