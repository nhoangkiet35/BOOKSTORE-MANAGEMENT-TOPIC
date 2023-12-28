from sqlalchemy import text, func, desc
from bookstore import db
from bookstore.models import Configuration, ImportTicket, Book, Category, Author, PaymentMethod, User, Order, \
    OrderDetails, BankingInformation


def get_configuration():
    return Configuration.query.first()


def save_ticket(url):
    ticket = ImportTicket(excel_url=url)
    db.session.add(ticket)
    db.session.commit()
    return ticket


def get_book_by_name(name):
    return Book.query.filter(Book.name.__eq__(name)).first()


def save_book(book):
    db.session.add(book)
    db.session.commit()


def get_category_by_name(name):
    return Category.query.filter(Category.name.__eq__(name)).first()


def save_category(category):
    db.session.add(category)
    db.session.commit()


def get_author_by_name(name):
    return Author.query.filter(Author.name.__eq__(name)).first()


def save_author(author):
    db.session.add(author)
    db.session.commit()


def save_ticket_details(ticket_details):
    db.session.add(ticket_details)
    db.session.commit()


def get_payment_method_by_id(id):
    return PaymentMethod.query.get(id)


def get_payment_method_all():
    return PaymentMethod.query.all()


def get_user_by_id(id):
    return User.query.get(id)


def save_user(user):
    db.session.add(user)
    db.session.commit()


def get_book_by_id(id):
    return Book.query.get(id)


def save_order(order):
    db.session.add(order)
    db.session.commit()


def save_order_details(order_detail):
    db.session.add(order_detail)
    db.session.commit()


def get_order_by_id(order_id):
    return Order.query.get(order_id)


def get_orders_by_customer_id(customer_id):
    return Order.query.filter_by(customer_id=customer_id).order_by(Order.id.asc()).all()


def save_banking_information(order_id, bank_transaction_number, vnpay_transaction_number, bank_code, card_type,
                             secure_hash):
    infor = BankingInformation(order_id=order_id, bank_transaction_number=bank_transaction_number,
                               vnpay_transaction_number=vnpay_transaction_number, bank_code=bank_code,
                               card_type=card_type, secure_hash=secure_hash)
    db.session.add(infor)
    db.session.commit()
    return infor


# def stat_book_by_month(month):
#     return db.session.execute(text("SELECT book.name, category.name AS category,  SUM(order_details.quantity) AS quantity "
#                                    "FROM  bookstore.book "
#                                    "JOIN bookstore.order_details "
#                                    "ON book.id = order_details.book_id "
#                                    "JOIN bookstore.order "
#                                    "ON order_details.order_id = bookstore.order.id "
#                                    "JOIN bookstore.category "
#                                    "ON book.category_id = category.id "
#                                    "WHERE month(bookstore.order.paid_date) = 2 "
#                                    "GROUP BY book.name "
#                                    "ORDER BY quantity"), {"month": month}).all()
def stat_book_by_month(month):
    return db.session.query(Book.name, Category.name, func.sum(OrderDetails.quantity).label("quantity")) \
        .join(Book, Book.id == OrderDetails.book_id) \
        .join(Order, OrderDetails.order_id == Order.id) \
        .join(Category, Book.category_id == Category.id) \
        .group_by(Book.name) \
        .filter(func.extract("month", Order.paid_date) == month) \
        .order_by(desc("quantity")) \
        .all()


# def stat_category_by_month(month):
#     return db.session.execute(text("SELECT category.name, count(order_details.book_id) AS number_of_purchases, SUM(order_details.quantity * order_details.unit_price) AS revenue "
#                                    "FROM  bookstore.category "
#                                    "LEFT JOIN bookstore.book ON category.id = book.category_id "
#                                    "LEFT JOIN bookstore.order_details ON book.id = order_details.book_id "
#                                    "JOIN bookstore.order ON order_details.order_id = bookstore.order.id "
#                                    "WHERE month(bookstore.order.paid_date) = :month "
#                                    "GROUP BY category.name "
#                                    "ORDER BY revenue DESC"), {"month": month}).all()
def stat_category_by_month(month):
    return db.session.query(Category.name, func.count(OrderDetails.book_id),
                            func.sum(OrderDetails.quantity * OrderDetails.unit_price).label("revenue")) \
        .join(Book, Category.id == Book.category_id) \
        .join(OrderDetails, Book.id == OrderDetails.book_id) \
        .join(Order, OrderDetails.order_id == Order.id) \
        .group_by(Category.name) \
        .filter(func.extract("month", Order.paid_date) == month) \
        .order_by(desc("revenue")) \
        .all()


# def statistic_revenue():
#     return db.session.execute(text("SELECT SUM(total_payment) AS revenue "
#                                    "FROM bookstore.order "
#                                    "GROUP BY month(paid_date) "
#                                    "ORDER BY month(paid_date)")).all()

def statistic_revenue():
    return db.session.query(func.sum(Order.total_payment).label("revenue")) \
        .group_by(func.extract("month", Order.paid_date)) \
        .order_by(desc("revenue")) \
        .all()
