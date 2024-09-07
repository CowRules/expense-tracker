'''expense_tracker URL Configuration
'''

from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . views import (auth, account, account_sync,
                            json, preset, tag, transaction)

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/transactions')),
    re_path(r'^transactions$', transaction.TransactionListView.as_view()),
    re_path(r'^transactions/add$', transaction.TransactionCreateView.as_view()),
    re_path(r'^transactions/(?P<pk>\d+)$',
        transaction.TransactionSubtransactionsListView.as_view()),
    re_path(r'^transactions/(?P<pk>\d+)/edit$',
        transaction.TransactionUpdateView.as_view()),
    re_path(r'^transactions/(?P<pk>\d+)/delete$',
        transaction.TransactionDeleteView.as_view()),

    re_path(r'^accounts$', account.AccountListView.as_view()),
    re_path(r'^accounts/(?P<pk>\d+)$',
        account.AccountSubtransactionsListView.as_view()),
    re_path(r'^accounts/(?P<pk>\d+)/edit$', account.AccountUpdateView.as_view()),
    re_path(r'^accounts/(?P<pk>\d+)/delete$', account.AccountDeleteView.as_view()),
    re_path(r'^accounts/add$', account.AccountCreateView.as_view()),

    re_path(r'^sync/(?P<pk>\d+)$',
        account_sync.AccountSyncDetailView.as_view()),
    re_path(r'^sync/(?P<pk>\d+)/edit$',
        account_sync.AccountSyncUpdateView.as_view()),
    re_path(r'^sync/(?P<pk>\d+)/delete$',
        account_sync.AccountSyncDeleteView.as_view()),
    re_path(r'^accounts/(?P<account_pk>\d+)/sync$',
        account_sync.AccountSyncCreateView.as_view()),

    re_path(r'^presets$', preset.PresetListView.as_view()),
    re_path(r'^presets/(?P<pk>\d+)$', preset.PresetDetailView.as_view()),
    re_path(r'^presets/(?P<pk>\d+)/edit$', preset.PresetUpdateView.as_view()),
    re_path(r'^presets/(?P<pk>\d+)/delete$', preset.PresetDeleteView.as_view()),
    re_path(r'^presets/add$', preset.PresetCreateView.as_view()),

    re_path(r'^tags$', tag.TagListView.as_view()),
    re_path(r'^tags/(?P<pk>\d+)$', tag.TagTransactionListView.as_view()),
    re_path(r'^tags/(?P<pk>\d+)/edit$', tag.TagUpdateView.as_view()),
    re_path(r'^tags/(?P<pk>\d+)/delete$', tag.TagDeleteView.as_view()),
    re_path(r'^tags/add$', tag.TagCreateView.as_view()),

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^user/login$', auth.login),
    re_path(r'^user/logout$', auth.logout),
    re_path(r'^user/profile$', auth.logged_in),
    re_path(r'^user/edit$', auth.user_edit),
]
