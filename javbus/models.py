from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify,
#   and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Genre(models.Model):
    g_id = models.AutoField(primary_key=True)
    genreid = models.CharField(db_column='genreID', unique=True, max_length=40, blank=True,
                               null=True)  # Field name made lowercase.
    genrename = models.TextField(db_column='genreName', blank=True, null=True)
    # Field name made lowercase.
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.genrename


class Images(models.Model):
    i_id = models.AutoField(primary_key=True)
    avnum = models.ForeignKey(on_delete=models.DO_NOTHING,
                              to='Movies', to_field='avnum',
                              related_name='t_images',
                              db_column='avNum',
                              blank=True,
                              null=True)
    # Field name made lowercase.
    imgurl = models.TextField(db_column='imgUrl', blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'images'


class MG(models.Model):
    m_g_id = models.AutoField(primary_key=True)
    avnum = models.ForeignKey(to='Movies',
                              to_field='avnum',
                              on_delete=models.DO_NOTHING,
                              related_name='t_mg',
                              db_column='avNum',
                              blank=True,
                              null=True)
    # Field name made lowercase.
    genreid = models.ForeignKey(to='Genre',
                                to_field='genreid',
                                on_delete=models.DO_NOTHING,
                                related_name='t_mg',
                                db_column='genreID',
                                blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_g'
        unique_together = (('avnum', 'genreid'),)


class MS(models.Model):
    m_s_id = models.AutoField(primary_key=True)
    avnum = models.ForeignKey(to='Movies',
                              to_field='avnum',
                              on_delete=models.DO_NOTHING,
                              related_name='t_ms',
                              db_column='avNum',
                              blank=True,
                              null=True)
    # Field name made lowercase.
    starid = models.ForeignKey(to='Stars',
                               to_field='starid',
                               on_delete=models.DO_NOTHING,
                               related_name='t_ms',
                               db_column='starID',
                               blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_s'
        unique_together = (('avnum', 'starid'),)


class Magnets(models.Model):
    ma_id = models.AutoField(primary_key=True)
    avnum = models.ForeignKey(to='Movies',
                              to_field='avnum',
                              on_delete=models.DO_NOTHING,
                              related_name='t_magnets',
                              db_column='avNum',
                              blank=True,
                              null=True)
    # Field name made lowercase.
    url = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    addtime = models.DateField(db_column='addTime', blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'magnets'


class Movies(models.Model):
    m_id = models.AutoField(primary_key=True)
    avnum = models.CharField(db_column='avNum', unique=True, max_length=40, blank=True, null=True)
    # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    coverimgurl = models.TextField(db_column='coverImgUrl', blank=True, null=True)
    # Field name made lowercase.
    thumbimgurl = models.TextField(db_column='thumbImgUrl', blank=True,
                                   null=True)  # Field name made lowercase.
    release = models.DateField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    producer = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class Stars(models.Model):
    s_id = models.AutoField(primary_key=True)
    starid = models.CharField(db_column='starID', unique=True, max_length=40, blank=True, null=True)
    # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    cups = models.TextField(blank=True, null=True)
    bust = models.IntegerField(blank=True, null=True)
    waist = models.IntegerField(blank=True, null=True)
    hip = models.IntegerField(blank=True, null=True)
    birthplace = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stars'
