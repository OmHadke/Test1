import React from "react";
import {
  SafeAreaView,
  ScrollView,
  StyleSheet,
  Text,
  View,
  Image,
  Pressable,
} from "react-native";

const dishes = [
  {
    id: "d1",
    name: "Grilled Veg Bowl",
    image: "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800",
    calories: 320,
    price: 299,
    category: "Main",
    recommendedFor: ["fitness", "vegan"],
  },
  {
    id: "d2",
    name: "Herb Paneer Skewers",
    image: "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
    calories: 280,
    price: 249,
    category: "Starter",
    recommendedFor: ["kids"],
  },
  {
    id: "d3",
    name: "Quinoa Salad",
    image: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800",
    calories: 260,
    price: 219,
    category: "Main",
    recommendedFor: ["diabetic", "fitness"],
  },
];

const bookings = [
  { id: "b1", time: "7:00 PM", seats: "Table for 2" },
  { id: "b2", time: "8:30 PM", seats: "Table for 4" },
  { id: "b3", time: "9:00 PM", seats: "Table for 6" },
];

export default function App() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.header}>
          <View>
            <Text style={styles.appTitle}>RMS Mobile</Text>
            <Text style={styles.subTitle}>QR menu • Booking • Order</Text>
          </View>
          <View style={styles.badge}>
            <Text style={styles.badgeText}>Restaurant Admin</Text>
          </View>
        </View>

        <View style={styles.sectionCard}>
          <Text style={styles.sectionTitle}>Restaurant Registration</Text>
          <Text style={styles.sectionBody}>
            Capture restaurant details, generate a unique ID, and share a QR that links to
            menu/{"{"}restaurantId{"}"}.
          </Text>
          <View style={styles.formRow}>
            <View style={styles.inputStub}>
              <Text style={styles.inputLabel}>Restaurant name</Text>
              <Text style={styles.inputValue}>FreshFork Kitchen</Text>
            </View>
            <View style={styles.inputStub}>
              <Text style={styles.inputLabel}>Opening hours</Text>
              <Text style={styles.inputValue}>11 AM – 11 PM</Text>
            </View>
          </View>
          <View style={styles.qrCard}>
            <Text style={styles.qrTitle}>QR Menu Link</Text>
            <Text style={styles.qrLink}>https://yourapp.com/menu/rms-3841</Text>
          </View>
        </View>

        <View style={styles.sectionCard}>
          <View style={styles.sectionHeaderRow}>
            <Text style={styles.sectionTitle}>Menu Highlights</Text>
            <Pressable style={styles.primaryButton}>
              <Text style={styles.primaryButtonText}>Add Dish</Text>
            </Pressable>
          </View>
          {dishes.map((dish) => (
            <View key={dish.id} style={styles.dishCard}>
              <Image source={{ uri: dish.image }} style={styles.dishImage} />
              <View style={styles.dishInfo}>
                <Text style={styles.dishName}>{dish.name}</Text>
                <Text style={styles.dishMeta}>
                  {dish.category} • {dish.calories} kcal
                </Text>
                <View style={styles.tagRow}>
                  {dish.recommendedFor.map((tag) => (
                    <View key={tag} style={styles.tag}>
                      <Text style={styles.tagText}>{tag}</Text>
                    </View>
                  ))}
                </View>
              </View>
              <View style={styles.dishActions}>
                <Text style={styles.price}>₹{dish.price}</Text>
                <Pressable style={styles.ghostButton}>
                  <Text style={styles.ghostButtonText}>Edit</Text>
                </Pressable>
              </View>
            </View>
          ))}
        </View>

        <View style={styles.sectionCard}>
          <Text style={styles.sectionTitle}>Customer Experience</Text>
          <View style={styles.row}>
            <View style={styles.statCard}>
              <Text style={styles.statValue}>QR Scan</Text>
              <Text style={styles.statLabel}>Menu access</Text>
            </View>
            <View style={styles.statCard}>
              <Text style={styles.statValue}>Pre-order</Text>
              <Text style={styles.statLabel}>Add to cart</Text>
            </View>
            <View style={styles.statCard}>
              <Text style={styles.statValue}>Pay</Text>
              <Text style={styles.statLabel}>COD/Razorpay</Text>
            </View>
          </View>
        </View>

        <View style={styles.sectionCard}>
          <View style={styles.sectionHeaderRow}>
            <Text style={styles.sectionTitle}>Table Bookings</Text>
            <Pressable style={styles.primaryButton}>
              <Text style={styles.primaryButtonText}>New Booking</Text>
            </Pressable>
          </View>
          {bookings.map((booking) => (
            <View key={booking.id} style={styles.bookingRow}>
              <View>
                <Text style={styles.bookingTime}>{booking.time}</Text>
                <Text style={styles.bookingSeats}>{booking.seats}</Text>
              </View>
              <Pressable style={styles.ghostButton}>
                <Text style={styles.ghostButtonText}>Confirm</Text>
              </Pressable>
            </View>
          ))}
        </View>

        <View style={styles.sectionCard}>
          <Text style={styles.sectionTitle}>Reviews Snapshot</Text>
          <View style={styles.reviewCard}>
            <Text style={styles.reviewScore}>4.6 ★</Text>
            <Text style={styles.reviewText}>
              “Great healthy options and quick service.”
            </Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "#f5f6fb",
  },
  container: {
    padding: 20,
    gap: 16,
  },
  header: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
  },
  appTitle: {
    fontSize: 24,
    fontWeight: "700",
    color: "#0f172a",
  },
  subTitle: {
    color: "#64748b",
    marginTop: 4,
  },
  badge: {
    backgroundColor: "#e0f2fe",
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 16,
  },
  badgeText: {
    color: "#0284c7",
    fontSize: 12,
    fontWeight: "600",
  },
  sectionCard: {
    backgroundColor: "#ffffff",
    borderRadius: 16,
    padding: 16,
    shadowColor: "#0f172a",
    shadowOpacity: 0.08,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 12,
    elevation: 3,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "700",
    marginBottom: 12,
    color: "#0f172a",
  },
  sectionBody: {
    color: "#475569",
    marginBottom: 12,
    lineHeight: 20,
  },
  formRow: {
    flexDirection: "row",
    gap: 12,
  },
  inputStub: {
    flex: 1,
    backgroundColor: "#f8fafc",
    borderRadius: 12,
    padding: 12,
  },
  inputLabel: {
    fontSize: 12,
    color: "#94a3b8",
    marginBottom: 4,
  },
  inputValue: {
    fontSize: 14,
    fontWeight: "600",
    color: "#0f172a",
  },
  qrCard: {
    marginTop: 12,
    padding: 12,
    backgroundColor: "#eef2ff",
    borderRadius: 12,
  },
  qrTitle: {
    fontSize: 12,
    color: "#6366f1",
    fontWeight: "600",
  },
  qrLink: {
    fontSize: 13,
    color: "#312e81",
    marginTop: 4,
  },
  sectionHeaderRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 12,
  },
  primaryButton: {
    backgroundColor: "#6366f1",
    paddingVertical: 8,
    paddingHorizontal: 14,
    borderRadius: 10,
  },
  primaryButtonText: {
    color: "#ffffff",
    fontWeight: "600",
    fontSize: 12,
  },
  dishCard: {
    flexDirection: "row",
    gap: 12,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: "#e2e8f0",
  },
  dishImage: {
    width: 72,
    height: 72,
    borderRadius: 12,
  },
  dishInfo: {
    flex: 1,
  },
  dishName: {
    fontSize: 16,
    fontWeight: "600",
    color: "#0f172a",
  },
  dishMeta: {
    fontSize: 12,
    color: "#64748b",
    marginTop: 4,
  },
  tagRow: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 6,
    marginTop: 8,
  },
  tag: {
    backgroundColor: "#f1f5f9",
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 999,
  },
  tagText: {
    fontSize: 10,
    color: "#475569",
  },
  dishActions: {
    justifyContent: "space-between",
    alignItems: "flex-end",
  },
  price: {
    fontSize: 14,
    fontWeight: "700",
    color: "#0f172a",
  },
  ghostButton: {
    borderWidth: 1,
    borderColor: "#cbd5f5",
    paddingVertical: 6,
    paddingHorizontal: 10,
    borderRadius: 10,
  },
  ghostButtonText: {
    fontSize: 12,
    color: "#6366f1",
    fontWeight: "600",
  },
  row: {
    flexDirection: "row",
    gap: 12,
  },
  statCard: {
    flex: 1,
    backgroundColor: "#f8fafc",
    borderRadius: 12,
    padding: 12,
    alignItems: "center",
  },
  statValue: {
    fontSize: 14,
    fontWeight: "700",
    color: "#0f172a",
  },
  statLabel: {
    fontSize: 11,
    color: "#64748b",
    marginTop: 6,
  },
  bookingRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: "#e2e8f0",
  },
  bookingTime: {
    fontSize: 15,
    fontWeight: "600",
    color: "#0f172a",
  },
  bookingSeats: {
    fontSize: 12,
    color: "#64748b",
    marginTop: 4,
  },
  reviewCard: {
    backgroundColor: "#f8fafc",
    borderRadius: 12,
    padding: 14,
  },
  reviewScore: {
    fontSize: 18,
    fontWeight: "700",
    color: "#0f172a",
  },
  reviewText: {
    fontSize: 12,
    color: "#475569",
    marginTop: 6,
  },
});
