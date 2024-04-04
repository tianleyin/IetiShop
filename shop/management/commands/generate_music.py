from django.core.management.base import BaseCommand
from faker import Faker
from faker_music import MusicProvider
from shop.models import Producto, Categoria 

class Command(BaseCommand):
    help = 'Generates fake products using faker_music'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(MusicProvider)

        # Crear nuevas categorías
        categorias_nuevas = ['Guitarras', 'Pianos', 'Baterías', 'Violines']
        nuevas_categorias_objs = []
        for nombre_categoria in categorias_nuevas:
            nueva_categoria = Categoria.objects.create(nombre=nombre_categoria)
            nuevas_categorias_objs.append(nueva_categoria)

        for _ in range(10):  # Generar 10 productos de ejemplo
            # Seleccionar una categoría aleatoria para cada producto
            categoria = fake.random_element(nuevas_categorias_objs)

            producto = Producto.objects.create(
                nombre=fake.music_instrument(),
                descripcion=fake.sentence(),
                precio=fake.random_number(digits=3),
                cantidad_disponible=fake.random_number(digits=2),
                categoria=categoria
            )

            self.stdout.write(self.style.SUCCESS(f'Producto generado: {producto.nombre}'))
