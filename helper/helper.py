from Fruitipedia.fruits.models import FruitModel
from Fruitipedia.profiles.models import ProfileModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def get_fruits():
    return FruitModel.objects.all()


def get_fruit(pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    return fruit
