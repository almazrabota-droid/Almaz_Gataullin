import tkinter as tk
from tkinter import messagebox, Listbox, END
import requests
import json

# Путь к файлу избранного
FAVORITES_FILE = "favorites.json"

# Загрузка избранных пользователей
def load_favorites():
    try:
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Сохранение избранных пользователей
def save_favorites(users):
    with open(FAVORITES_FILE, "w") as f:
        json.dump(users, f, indent=2)

# Поиск пользователя через GitHub API
def search_user():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Ошибка", "Поле поиска не должно быть пустым!")
        return

    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            user_data = response.json()
            display_user(user_data)
        else:
            messagebox.showerror("Ошибка", f"Пользователь {username} не найден.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось выполнить запрос: {e}")

# Отображение пользователя в списке
def display_user(user):
    listbox.insert(END, f"{user['login']} ({user['name']})")
    # Добавляем в избранное при двойном клике
    listbox.bind("<Double-Button-1>", lambda e: add_to_favorites(user))

# Добавление пользователя в избранное
def add_to_favorites(user):
    favorites = load_favorites()
   
