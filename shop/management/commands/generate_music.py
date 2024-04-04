from django.core.management.base import BaseCommand
from faker import Faker
from faker_music import MusicProvider
from shop.models import Producto, Categoria 

class Command(BaseCommand):
    help = 'Generates fake products using faker_music'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(MusicProvider)

        # Obtén una lista de todas las categorías disponibles
        categorias = Categoria.objects.all()

        for _ in range(10):  # Generar 10 productos de ejemplo
            # Selecciona una categoría aleatoria para cada producto
            categoria = fake.random_element(categorias)

            producto = Producto.objects.create(
                nombre=fake.music_instrument(),
                descripcion=fake.sentence(),
                precio=fake.random_number(digits=3),
                cantidad_disponible=fake.random_number(digits=2),
                categoria=categoria
            )

            self.stdout.write(self.style.SUCCESS(f'Producto generado: {producto.nombre}'))
