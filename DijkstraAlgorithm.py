import pygame
import sys

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Nodo:
    def __init__(self, etiqueta, posicion):
        self.etiqueta = etiqueta
        self.conexiones = {}
        self.valor = float('inf')
        self.nodoAnterior = None
        self.posicion = posicion
        self.colorActivo = BLUE
        self.colorInactivo = BLACK
        self.activo = False
        self.connectionsRect = {}

    def agregarConexion(self, nodo, peso):
        self.conexiones[nodo] = peso
        self.draw_connection(nodo)
        
    def dibujarNodo(self):
        if self.activo:
            pygame.draw.circle(screen, self.colorActivo, self.posicion, 15)
        else:
            pygame.draw.circle(screen, self.colorInactivo, self.posicion, 15)
        text = font.render(self.etiqueta, True, WHITE)
        text_rect = text.get_rect(center=(self.posicion[0], self.posicion[1]))
        screen.blit(text, text_rect)
        
    def dibujarNodo2(self):
        pygame.draw.circle(screen, GREEN, self.posicion, 15)
        text = font.render(self.etiqueta, True, WHITE)
        text_rect = text.get_rect(center=(self.posicion[0], self.posicion[1]))
        screen.blit(text, text_rect)
    
    def draw_connection(self, nodo):
        x1, y1 = self.posicion
        x2, y2 = nodo.posicion
    
        line_x = (x1 + x2) / 2
        line_y = (y1 + y2) / 2
            
        text = font.render(str(self.conexiones[nodo]), True, BLACK)
        text_rect = text.get_rect(center=(line_x, line_y))
        
        if nodo in self.connectionsRect:
            pygame.draw.rect(screen, WHITE, self.connectionsRect[nodo])
        
        self.connectionsRect[nodo] = text_rect
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)
        screen.blit(text, text_rect)
        
    def draw_connection2(self, nodo):
        x1, y1 = self.posicion
        x2, y2 = nodo.posicion
    
        line_x = (x1 + x2) / 2
        line_y = (y1 + y2) / 2
            
        text = font.render(str(self.conexiones[nodo]), True, BLACK)
        text_rect = text.get_rect(center=(line_x, line_y))
        
        if nodo in self.connectionsRect:
            pygame.draw.rect(screen, WHITE, self.connectionsRect[nodo])
        
        self.connectionsRect[nodo] = text_rect
        pygame.draw.line(screen, GREEN, (x1, y1), (x2, y2), 2)
        screen.blit(text, text_rect)
        
    
    def is_clicked(self, click_pos):
        x, y = self.posicion
        dist_squared = (x - click_pos[0]) ** 2 + (y - click_pos[1]) ** 2
        return dist_squared <= 15 ** 2

def dijkstra(grafo, nodoInicial):
    nodoInicial.valor = 0
    nodosAbiertos = list(grafo.values())
    for nodo in nodosAbiertos:
        nodo.nodoAnterior = None
        if nodo != nodoInicial:
            nodo.valor = float('inf')
    nodosCerrados = []

    while nodosAbiertos:
        nodoActivo = min(nodosAbiertos, key=lambda node: node.valor)
        nodosAbiertos.remove(nodoActivo)
        nodosCerrados.append(nodoActivo)

        for nodo, peso in nodoActivo.conexiones.items():
            distancia = nodoActivo.valor + peso
            if distancia < nodo.valor:
                nodo.valor = distancia
                nodo.nodoAnterior = nodoActivo

grafo = {}
nodoInicial = "NA"
nodoFinal = "NA"

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Editor")

# Font for node letters
font = pygame.font.Font(None, 36)
    
def get_input():
    input_text = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    if not input_text:  # No numbers entered
                        return '0'
                    else:
                        input_active = False
                elif event.unicode.isnumeric():
                    input_text += event.unicode

    return input_text

# Function to clear the screen
def clear_screen():
    nodosSeleccionados.clear()
    grafo.clear()
    screen.fill(WHITE)
    # Draw the clear button
    pygame.draw.rect(screen, RED, clear_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Clear", True, WHITE)
    text_rect1 = text.get_rect(center=(clear_button.x + clear_button.width // 2, clear_button.y + clear_button.height // 2))
    screen.blit(text, text_rect1)
    # Draw the "Initial Node" button
    pygame.draw.rect(screen, BLACK, initial_node_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Initial Node: NA", True, WHITE)
    text_rect2 = text.get_rect(center=(initial_node_button.x + initial_node_button.width // 2, initial_node_button.y + initial_node_button.height // 2))
    screen.blit(text, text_rect2)
    # Draw the "Final Node" button
    pygame.draw.rect(screen, BLACK, final_node_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Final Node: NA", True, WHITE)
    text_rect3 = text.get_rect(center=(final_node_button.x + final_node_button.width // 2, final_node_button.y + final_node_button.height // 2))
    screen.blit(text, text_rect3)
    # Draw the "Calculate Route" button
    pygame.draw.rect(screen, GREEN, calculate_route_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Calculate Route", True, WHITE)
    text_rect4 = text.get_rect(center=(calculate_route_button.x + calculate_route_button.width // 2, calculate_route_button.y + calculate_route_button.height // 2))
    screen.blit(text, text_rect4)

    
def crearNodo(posicion):
    letra = chr(ord('A') + len(grafo))
    grafo[letra] = Nodo(letra, posicion)
    grafo[letra].dibujarNodo()
    
def colorearRuta(path):
    if len(path)==1:
        path[0].dibujarNodo2()
    for i in range(len(path)-1):
        path[i].draw_connection2(path[i+1])
        path[i].dibujarNodo2()
        if i == len(path)-2:
            path[i+1].dibujarNodo2()
            
def quitarRutaColoreada(grafo):
    for nodo in grafo.values():
        nodo.dibujarNodo()
        for conexion in nodo.conexiones:
            nodo.draw_connection(conexion)
    
# Create a clear button
clear_button = pygame.Rect(10, 10, 80, 30)

# Create an "Initial Node" button
initial_node_button = pygame.Rect(100, 10, 200, 30)

# Create a "Final Node" button
final_node_button = pygame.Rect(310, 10, 200, 30)

# Create a "Calculate Route" button
calculate_route_button = pygame.Rect(520, 10, 200, 30)

nodosSeleccionados = []
screen.fill(WHITE)
# Draw the clear button
pygame.draw.rect(screen, RED, clear_button)
font = pygame.font.Font(None, 36)
text = font.render("Clear", True, WHITE)
text_rect1 = text.get_rect(center=(clear_button.x + clear_button.width // 2, clear_button.y + clear_button.height // 2))
screen.blit(text, text_rect1)
# Draw the "Initial Node" button
pygame.draw.rect(screen, BLACK, initial_node_button)
font = pygame.font.Font(None, 36)
text = font.render("Initial Node: NA", True, WHITE)
text_rect2 = text.get_rect(center=(initial_node_button.x + initial_node_button.width // 2, initial_node_button.y + initial_node_button.height // 2))
screen.blit(text, text_rect2)
# Draw the "Final Node" button
pygame.draw.rect(screen, BLACK, final_node_button)
font = pygame.font.Font(None, 36)
text = font.render("Final Node: NA", True, WHITE)
text_rect3 = text.get_rect(center=(final_node_button.x + final_node_button.width // 2, final_node_button.y + final_node_button.height // 2))
screen.blit(text, text_rect3)
# Draw the "Calculate Route" button
pygame.draw.rect(screen, WHITE, calculate_route_button)
font = pygame.font.Font(None, 36)
text = font.render("Calculate Route", True, WHITE)
text_rect4 = text.get_rect(center=(calculate_route_button.x + calculate_route_button.width // 2, calculate_route_button.y + calculate_route_button.height // 2))
screen.blit(text, text_rect4)

selectingInitialNode = False
selectingFinalNode = False
while True:
    if nodoInicial != "NA" and nodoFinal != "NA":
        pygame.draw.rect(screen, GREEN, calculate_route_button)
        font = pygame.font.Font(None, 36)
        text = font.render("Calculate Route", True, WHITE)
        text_rect4 = text.get_rect(center=(calculate_route_button.x + calculate_route_button.width // 2, calculate_route_button.y + calculate_route_button.height // 2))
        screen.blit(text, text_rect4)
    else:
        pygame.draw.rect(screen, WHITE, calculate_route_button)
        font = pygame.font.Font(None, 36)
        text = font.render("Calculate Route", True, WHITE)
        text_rect4 = text.get_rect(center=(calculate_route_button.x + calculate_route_button.width // 2, calculate_route_button.y + calculate_route_button.height // 2))
        screen.blit(text, text_rect4)
    if selectingInitialNode:
        pygame.draw.rect(screen, BLUE, initial_node_button)
    else:
        pygame.draw.rect(screen, BLACK, initial_node_button)
    font = pygame.font.Font(None, 36)
    if nodoInicial == "NA":
        text = font.render("Initial Node: NA", True, WHITE)
    else:
        text = font.render("Initial Node: "+nodoInicial.etiqueta, True, WHITE)
    text_rect2 = text.get_rect(center=(initial_node_button.x + initial_node_button.width // 2, initial_node_button.y + initial_node_button.height // 2))
    screen.blit(text, text_rect2)
    # Draw the "Final Node" button
    if selectingFinalNode:
        pygame.draw.rect(screen, BLUE, final_node_button)
    else:
        pygame.draw.rect(screen, BLACK, final_node_button)
    font = pygame.font.Font(None, 36)
    if nodoFinal == "NA":
        text = font.render("Final Node: NA", True, WHITE)
    else:
        text = font.render("Final Node: "+ nodoFinal.etiqueta, True, WHITE)
    text_rect3 = text.get_rect(center=(final_node_button.x + final_node_button.width // 2, final_node_button.y + final_node_button.height // 2))
    screen.blit(text, text_rect3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button to add nodes
                if clear_button.collidepoint(event.pos):
                    quitarRutaColoreada(grafo)
                    clear_screen()
                    selectingInitialNode = False
                    selectingFinalNode = False
                    nodoInicial = "NA"
                    nodoFinal = "NA"
                elif initial_node_button.collidepoint(event.pos):
                    selectingInitialNode = True
                    selectingFinalNode = False
                    for n in nodosSeleccionados:
                        n.activo = False
                        n.dibujarNodo()
                    nodosSeleccionados = []
                    pygame.draw.rect(screen, BLUE, initial_node_button)
                    font = pygame.font.Font(None, 36)
                    if nodoInicial == "NA":
                        text = font.render("Initial Node: NA", True, WHITE)
                    else:
                        text = font.render("Initial Node: "+nodoInicial.etiqueta, True, WHITE)
                    text_rect2 = text.get_rect(center=(initial_node_button.x + initial_node_button.width // 2, initial_node_button.y + initial_node_button.height // 2))
                    screen.blit(text, text_rect2)
                    # Draw the "Final Node" button
                    pygame.draw.rect(screen, BLACK, final_node_button)
                    font = pygame.font.Font(None, 36)
                    if nodoFinal == "NA":
                        text = font.render("Final Node: NA", True, WHITE)
                    else:
                        text = font.render("Final Node: "+nodoFinal.etiqueta, True, WHITE)
                    text_rect3 = text.get_rect(center=(final_node_button.x + final_node_button.width // 2, final_node_button.y + final_node_button.height // 2))
                    screen.blit(text, text_rect3)
                elif final_node_button.collidepoint(event.pos):
                    selectingInitialNode = False
                    selectingFinalNode = True
                    for n in nodosSeleccionados:
                        n.activo = False
                        n.dibujarNodo()
                    nodosSeleccionados = []
                    pygame.draw.rect(screen, BLACK, initial_node_button)
                    font = pygame.font.Font(None, 36)
                    if nodoInicial == "NA":
                        text = font.render("Initial Node: NA", True, WHITE)
                    else:
                        text = font.render("Initial Node: "+nodoInicial.etiqueta, True, WHITE)
                    text_rect2 = text.get_rect(center=(initial_node_button.x + initial_node_button.width // 2, initial_node_button.y + initial_node_button.height // 2))
                    screen.blit(text, text_rect2)
                    # Draw the "Final Node" button
                    pygame.draw.rect(screen, BLUE, final_node_button)
                    font = pygame.font.Font(None, 36)
                    if nodoFinal == "NA":
                        text = font.render("Final Node: NA", True, WHITE)
                    else:
                        text = font.render("Final Node: "+nodoFinal.etiqueta, True, WHITE)
                    text_rect3 = text.get_rect(center=(final_node_button.x + final_node_button.width // 2, final_node_button.y + final_node_button.height // 2))
                    screen.blit(text, text_rect3)
                elif calculate_route_button.collidepoint(event.pos):
                    if nodoInicial == "NA" or nodoFinal == "NA":
                        pass
                    elif nodoInicial == nodoFinal:
                        quitarRutaColoreada(grafo)
                        colorearRuta([nodoInicial])
                        print(f'Distancia más corta desde {nodoInicial.etiqueta} a {nodoFinal.etiqueta}: 0')
                        print(f'Ruta más corta desde {nodoInicial.etiqueta} a {nodoFinal.etiqueta}: {nodoInicial.etiqueta}')
                    else:
                        dijkstra(grafo, nodoInicial)
                        if nodoFinal.valor == float('inf'):
                            print("No es posible llegar del nodo "+nodoInicial.etiqueta+" al nodo "+nodoFinal.etiqueta)
                        else:
                            # Imprimir la distancia más corta desde el nodo de inicio al nodo final
                            print(f'Distancia más corta desde {nodoInicial.etiqueta} a {nodoFinal.etiqueta}: {nodoFinal.valor}')
                            # Imprimir la ruta más corta desde el nodo de inicio al nodo final
                            path = []
                            path2 = []
                            nodo = nodoFinal
                            while nodo is not None:
                                path2.insert(0, nodo)
                                path.insert(0, nodo.etiqueta)
                                nodo = nodo.nodoAnterior
                            if nodoInicial.nodoAnterior != None and nodoInicial.nodoAnterior.etiqueta in path:
                                path.remove(nodoInicial.nodoAnterior.etiqueta)
                            quitarRutaColoreada(grafo)
                            colorearRuta(path2)
                            print(f'Ruta más corta desde {nodoInicial.etiqueta} a {nodoFinal.etiqueta}: {" -> ".join(path)}')
                else:
                    clickOnNode = False
                    for nodo in grafo.values():
                        if nodo.is_clicked(event.pos):
                            clickOnNode = True
                            if selectingInitialNode:
                                quitarRutaColoreada(grafo)
                                nodoInicial = nodo
                                selectingInitialNode = False
                            elif selectingFinalNode:
                                quitarRutaColoreada(grafo)
                                nodoFinal = nodo
                                selectingFinalNode = False
                            else:
                                quitarRutaColoreada(grafo)
                                nodo.activo = True
                                nodo.dibujarNodo()
                                pygame.display.flip()  # Update the screen
                                if nodo in nodosSeleccionados:
                                    nodo.activo = False
                                    nodosSeleccionados = []
                                else:
                                    nodosSeleccionados.append(nodo)
                                    if len(nodosSeleccionados) == 2:
                                        p = int(get_input())
                                        nodosSeleccionados[0].agregarConexion(nodosSeleccionados[1], p)
                                        nodosSeleccionados[1].agregarConexion(nodosSeleccionados[0], p)
                                        nodosSeleccionados[0].activo = False
                                        nodosSeleccionados[0].dibujarNodo()
                                        nodosSeleccionados[1].activo = False
                                        nodosSeleccionados[1].dibujarNodo()
                                        nodosSeleccionados = []
                            break
                    if not clickOnNode:
                        quitarRutaColoreada(grafo)
                        selectingInitialNode = False
                        selectingFinalNode = False
                        crearNodo(event.pos)
                        for n in nodosSeleccionados:
                            n.activo = False
                            n.dibujarNodo()
                        nodosSeleccionados = []
                        pygame.draw.rect(screen, BLACK, initial_node_button)
                        font = pygame.font.Font(None, 36)
                        if nodoInicial == "NA":
                            text = font.render("Initial Node: NA", True, WHITE)
                        else:
                            text = font.render("Initial Node: "+nodoInicial.etiqueta, True, WHITE)
                        text_rect2 = text.get_rect(center=(initial_node_button.x + initial_node_button.width // 2, initial_node_button.y + initial_node_button.height // 2))
                        screen.blit(text, text_rect2)
                        # Draw the "Final Node" button
                        pygame.draw.rect(screen, BLACK, final_node_button)
                        font = pygame.font.Font(None, 36)
                        if nodoFinal == "NA":
                            text = font.render("Final Node: NA", True, WHITE)
                        else:
                            text = font.render("Final Node: "+nodoFinal.etiqueta, True, WHITE)
                        text_rect3 = text.get_rect(center=(final_node_button.x + final_node_button.width // 2, final_node_button.y + final_node_button.height // 2))
                        screen.blit(text, text_rect3)
                        
    pygame.display.flip()  # Update the screen