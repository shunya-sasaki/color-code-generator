# Color Code Generator

![python](https://img.shields.io/badge/python-gray?logo=python&labelColor=gray&logoColor=white)

## 📦 Requirements

- Python 3.11 or later
- uv (optional)

## ⚙️ Setup

**Option 1. uv**:

```sh
uv venv
uv pip install git@github.com:shunya-sasaki/colorcode-generator.git
```

## 🚀 Usage

Create config file `config.json` as the following.

```json
{
  "ratios": [-0.9, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 0.9],
  "colors": [
    {
      "name": "white",
      "hex": "#ffffff"
    },
    {
      "name": "black",
      "hex": "#000000"
    },
    {
      "name": "gray",
      "hex": "#999999"
    }
  ]
}
```

Run the following command to create color code files.

---

Option 1. uv:

```sh
uv run ccg-create-colors
```

---

Option 2. pip (venv):

```sh
ccg-create-colors
```

---

## 📄 License

[MIT License](./LICENSE)
