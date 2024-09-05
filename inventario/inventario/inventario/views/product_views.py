from django.shortcuts import render, redirect, get_object_or_404
from inventario.models.product import Product
from ..forms import ProductForm

# Vista para agregar un producto
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto
            return redirect('list_products')  # Redirige a la lista de productos
    else:
        form = ProductForm()
    return render(request, 'app/add_product.html', {'form': form})

# Vista para listar productos
def list_products(request):
    products = Product.objects.all()  # Obtiene todos los productos
    return render(request, 'app/list_products.html', {'products': products})

# Vista para confirmar y eliminar un producto
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':  # Solo eliminar cuando se envíe una confirmación con método POST
        product.delete()
        return redirect('list_products')  # Redirige a la lista de productos después de eliminar
    
    return render(request, 'app/confirm_delete.html', {'product': product})  # Muestra confirmación

# Vista para editar un producto
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Obtiene el producto o muestra 404 si no existe
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)  # Cargamos el producto actual en el formulario
        if form.is_valid():
            form.save()  # Guardamos los cambios
            return redirect('list_products')  # Redirigimos a la lista de productos después de guardar
    else:
        form = ProductForm(instance=product)  # Cargamos los datos del producto en el formulario
    return render(request, 'app/edit_product.html', {'form': form, 'product': product})

