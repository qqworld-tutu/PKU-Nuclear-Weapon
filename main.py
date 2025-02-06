import tkinter as tk
from tkinter import messagebox, filedialog
import csv

class CSVQueryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV查询工具")

        # 初始化变量
        self.file_path = None
        self.data = []

        # 创建界面
        self.create_widgets()

    def create_widgets(self):
        # 文件选择
        self.file_label = tk.Label(self.root, text="请选择CSV文件：")
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(self.root, text="浏览", command=self.load_csv)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # 查询部分
        self.query_label = tk.Label(self.root, text="查询条件：")
        self.query_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.name_label = tk.Label(self.root, text="姓名：")
        self.name_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)

        self.unit_label = tk.Label(self.root, text="单位：")
        self.unit_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.unit_entry = tk.Entry(self.root)
        self.unit_entry.grid(row=3, column=1, padx=10, pady=5)

        self.role_label = tk.Label(self.root, text="人员类别：")
        self.role_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.role_entry = tk.Entry(self.root)
        self.role_entry.grid(row=4, column=1, padx=10, pady=5)

        self.initials_label = tk.Label(self.root, text="首字母：")
        self.initials_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.initials_entry = tk.Entry(self.root)
        self.initials_entry.grid(row=5, column=1, padx=10, pady=5)

        self.query_button = tk.Button(self.root, text="查询", command=self.query_data)
        self.query_button.grid(row=6, column=1, padx=10, pady=10)

        # 显示结果
        self.result_text = tk.Text(self.root, height=10, width=60)
        self.result_text.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    def load_csv(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, self.file_path)
            self.load_data()

    def load_data(self):
        self.data = []
        try:
            with open(self.file_path, mode="r", newline="", encoding="gbk") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.data.append(row)
            messagebox.showinfo("成功", "CSV文件加载成功！")
        except Exception as e:
            messagebox.showerror("错误", f"加载CSV文件时出错：{e}")

    def query_data(self):
        name = self.name_entry.get().strip()
        unit = self.unit_entry.get().strip()
        role = self.role_entry.get().strip()
        initials = self.initials_entry.get().strip()

        if not self.data:
            messagebox.showwarning("警告", "请先加载CSV文件！")
            return

        result = []
        for item in self.data:
            if (not name or item.get("姓名") == name) and \
               (not unit or item.get("单位") == unit) and \
               (not role or item.get("人员类别") == role) and \
               (not initials or item.get("首字母") == initials):
                result.append(f"姓名：{item.get('姓名')}, 单位：{item.get('单位')}, 人员类别：{item.get('人员类别')}\n")

        if result:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "".join(result))
        else:
            messagebox.showinfo("未找到", "未找到匹配的记录！")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVQueryApp(root)
    root.mainloop()