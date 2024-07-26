class Cart():
    def __init__(Self, request):
        Self.session = request.session

        # get session key if it exists

        cart = Self.session.get('session_key')
        # if user is new, no session key
        if 'session_key' not in request.session:
            cart = Self.session['session_key'] = {} 

        # make sure the cart is available on all pages

        Self.cart = cart



    def add(Self, product):
        product_id = str(product.id)

        # logic
        if product_id in Self.cart:
            pass
        else:
            Self.cart[product_id] = {'price': str(product.price)}

        Self.session.modified = True

    def __len__(self):
        return len(self.cart)
