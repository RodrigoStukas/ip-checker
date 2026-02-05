import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from src.network.ip_checker import obter_hostname, obter_ip_redecorp, verificar_ip

class WidgetIP:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Checker")
        
        # Define tamanho da bolinha
        self.size = 40
        self.root.geometry(f"{self.size}x{self.size}")
        self.root.configure(bg="white")
        self.root.attributes("-alpha", 1.0)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.attributes("-transparentcolor", "white")
        
        # Posição inicial (canto inferior direito)
        self.x = self.root.winfo_screenwidth() - self.size - 20
        self.y = self.root.winfo_screenheight() - self.size - 80
        self.root.geometry(f"{self.size}x{self.size}+{int(self.x)}+{int(self.y)}")
        
        # Variáveis para drag
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.is_dragging = False
        
        # Canvas para desenhar a bolinha
        self.canvas = tk.Canvas(self.root, width=self.size, height=self.size, bg="white", highlightthickness=0, cursor="hand2")
        self.canvas.pack(fill="both", expand=True)
        
        # Carregar e exibir a imagem
        self.carregar_imagem()
        
        # Eventos de mouse
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Double-1>", self.abrir_janela_info)
        self.canvas.bind("<Button-3>", self.mostrar_menu)
        
        # Atualizar status a cada 10 segundos
        self.atualizar()
    
    def carregar_imagem(self):
        # Caminho da imagem
        img_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'ip_icon.png')
        
        try:
            # Carregar a imagem
            img = Image.open(img_path).convert("RGBA")
            
            # Redimensionar para o tamanho da bolinha
            img = img.resize((self.size, self.size), Image.Resampling.LANCZOS)
            
            # Converter para PhotoImage do tkinter
            self.photo = ImageTk.PhotoImage(img)
            
            # Colocar a imagem no canvas
            self.canvas.create_image(self.size // 2, self.size // 2, image=self.photo)
        
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            self.canvas.create_text(self.size // 2, self.size // 2, text="?", font=("Arial", 14, "bold"), fill="red")
    
    def atualizar(self):
        # Atualizar periodicamente
        self.root.after(10000, self.atualizar)
    
    def on_press(self, event):
        self.drag_start_x = event.x_root - self.root.winfo_x()
        self.drag_start_y = event.y_root - self.root.winfo_y()
        self.is_dragging = False
    
    def on_drag(self, event):
        self.is_dragging = True
        x = event.x_root - self.drag_start_x
        y = event.y_root - self.drag_start_y
        self.root.geometry(f"+{x}+{y}")
    
    def on_release(self, event):
        if not self.is_dragging:
            self.abrir_janela_info(event)
    
    def abrir_janela_info(self, event=None):
        ip_redecorp = obter_ip_redecorp()
        hostname = obter_hostname()
        
        janela = tk.Toplevel(self.root)
        janela.title("Informações de Rede")
        janela.geometry("550x400")
        janela.resizable(False, False)
        janela.configure(bg="#f5f5f5")
        
        # Título com imagem
        frame_titulo = tk.Frame(janela, bg="#f5f5f5")
        frame_titulo.pack(pady=10)
        
        # Carregar e exibir a imagem da bolinha no popup
        img_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'ip_icon.png')
        try:
            img = Image.open(img_path).resize((80, 80), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame_titulo, image=img_tk, bg="#f5f5f5")
            img_label.image = img_tk  # Manter referência
            img_label.pack()
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
        
        titulo = tk.Label(frame_titulo, text="📊 Informações da Máquina", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333")
        titulo.pack(pady=5)
        
        if ip_redecorp:
            frame_info = tk.LabelFrame(janela, text="Dados da Rede Corporativa", font=("Arial", 11, "bold"), bg="white", padx=15, pady=15)
            frame_info.pack(fill="both", expand=True, padx=10, pady=5)
            
            tk.Label(frame_info, text=f"Computador: {hostname}", font=("Arial", 11), bg="white", justify="left").pack(anchor="w", pady=5)
            tk.Label(frame_info, text=f"IP Corporativo: {ip_redecorp}", font=("Courier", 12, "bold"), bg="white", fg="#4CAF50", justify="left").pack(anchor="w", pady=5)
            
            frame_botoes = tk.Frame(janela, bg="#f5f5f5")
            frame_botoes.pack(fill="x", padx=10, pady=10)
            
            btn_copiar = tk.Button(frame_botoes, text="📋 Copiar IP", command=lambda: self.copiar_ip(ip_redecorp), bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=15, pady=8)
            btn_copiar.pack(side="left", padx=5)
            
            btn_fechar = tk.Button(frame_botoes, text="❌ Fechar", command=janela.destroy, bg="#f44336", fg="white", font=("Arial", 10, "bold"), padx=15, pady=8)
            btn_fechar.pack(side="right", padx=5)
        else:
            frame_aviso = tk.LabelFrame(janela, text="⚠️ Aviso", font=("Arial", 11, "bold"), bg="#fff3cd", padx=15, pady=15)
            frame_aviso.pack(fill="both", expand=True, padx=10, pady=5)
            
            tk.Label(frame_aviso, text=f"Computador: {hostname}", font=("Arial", 11), bg="#fff3cd", justify="left").pack(anchor="w", pady=5)
            tk.Label(frame_aviso, text="Nenhum IP corporativo detectado", font=("Arial", 11, "bold"), bg="#fff3cd", fg="#856404", justify="center").pack(pady=10)
            tk.Label(frame_aviso, text="Ligue a VPN para obter IP da rede corporativa", font=("Arial", 10), bg="#fff3cd", fg="#856404", justify="center").pack(pady=5)
            
            btn_fechar = tk.Button(janela, text="❌ Fechar", command=janela.destroy, bg="#f44336", fg="white", font=("Arial", 10, "bold"), padx=15, pady=8)
            btn_fechar.pack(pady=10)
    
    def copiar_ip(self, ip):
        self.root.clipboard_clear()
        self.root.clipboard_append(ip)
        messagebox.showinfo("Sucesso", f"IP copiado para a área de transferência:\n{ip}")
    
    def mostrar_menu(self, event):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Abrir", command=self.abrir_janela_info)
        menu.add_separator()
        menu.add_command(label="Sair", command=self.root.quit)
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

def iniciar_popup():
    root = tk.Tk()
    widget = WidgetIP(root)
    root.mainloop()
