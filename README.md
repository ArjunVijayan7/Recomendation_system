# 🧠 AI-Powered Course Recommendation System

This project builds an intelligent course recommender using semantic embeddings and PostgreSQL (with `pgvector`). It recommends courses based on title, organization, and difficulty — and ranks them by rating and popularity.

---

## 🚀 Features

- Embeds course metadata using `sentence-transformers`
- Stores embeddings and metadata in PostgreSQL
- Computes similarity using cosine distance
- Ranks results based on rating and enrollment count
- Supports UUID-based unique course IDs

---

## 📦 Project Structure

