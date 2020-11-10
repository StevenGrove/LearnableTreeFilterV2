#!/usr/bin/python3
# -*- coding:utf-8 -*-

from torch.optim import lr_scheduler

from cvpods.utils.registry import Registry

from .lr_scheduler import PolyLR, WarmupCosineLR, WarmupMultiStepLR

SCHEDULER_BUILDER = Registry("LRScheduler builder")


@SCHEDULER_BUILDER.register()
class BaseSchedulerBuilder:

    @staticmethod
    def build(optimizer, cfg):
        raise NotImplementedError


@SCHEDULER_BUILDER.register()
class WarmupMultiStepLRBuilder(BaseSchedulerBuilder):

    @staticmethod
    def build(optimizer, cfg):
        scheduler = WarmupMultiStepLR(
            optimizer,
            cfg.SOLVER.LR_SCHEDULER.STEPS,
            cfg.SOLVER.LR_SCHEDULER.GAMMA,
            warmup_factor=cfg.SOLVER.LR_SCHEDULER.WARMUP_FACTOR,
            warmup_iters=cfg.SOLVER.LR_SCHEDULER.WARMUP_ITERS,
            warmup_method=cfg.SOLVER.LR_SCHEDULER.WARMUP_METHOD,
        )
        return scheduler


@SCHEDULER_BUILDER.register()
class WarmupCosineLRBuilder(BaseSchedulerBuilder):

    @staticmethod
    def build(optimizer, cfg):
        max_iter = cfg.SOLVER.LR_SCHEDULER.MAX_ITER
        max_epoch = cfg.SOLVER.LR_SCHEDULER.MAX_EPOCH
        iters_per_epoch = None if max_epoch is None else max_iter // max_epoch

        scheduler = WarmupCosineLR(
            optimizer,
            cfg.SOLVER.LR_SCHEDULER.MAX_ITER,
            warmup_factor=cfg.SOLVER.LR_SCHEDULER.WARMUP_FACTOR,
            warmup_iters=cfg.SOLVER.LR_SCHEDULER.WARMUP_ITERS,
            warmup_method=cfg.SOLVER.LR_SCHEDULER.WARMUP_METHOD,
            iters_per_epoch=iters_per_epoch,
        )
        return scheduler


@SCHEDULER_BUILDER.register()
class PolyLRBuilder(BaseSchedulerBuilder):

    @staticmethod
    def build(optimizer, cfg):
        return PolyLR(
            optimizer,
            cfg.SOLVER.LR_SCHEDULER.MAX_ITER,
            cfg.SOLVER.LR_SCHEDULER.POLY_POWER,
            warmup_factor=cfg.SOLVER.LR_SCHEDULER.WARMUP_FACTOR,
            warmup_iters=cfg.SOLVER.LR_SCHEDULER.WARMUP_ITERS,
            warmup_method=cfg.SOLVER.LR_SCHEDULER.WARMUP_METHOD,
        )


@SCHEDULER_BUILDER.register()
class LambdaLRBuilder(BaseSchedulerBuilder):

    @staticmethod
    def build(optimizer, cfg):
        return lr_scheduler.LambdaLR(
            optimizer,
            cfg.SOLVER.LR_SCHEDULER.LAMBDA_SCHEDULE
        )


@SCHEDULER_BUILDER.register()
class OneCycleLRBuilder(BaseSchedulerBuilder):

    @staticmethod
    def build(optimizer, cfg):
        return lr_scheduler.OneCycleLR(
            optimizer,
            cfg.SOLVER.LR_SCHEDULER.MAX_LR,
            total_steps=cfg.SOLVER.LR_SCHEDULER.MAX_ITER,
            pct_start=cfg.SOLVER.LR_SCHEDULER.PCT_START,
            base_momentum=cfg.SOLVER.LR_SCHEDULER.BASE_MOM,
            max_momentum=cfg.SOLVER.LR_SCHEDULER.MAX_MOM,
            div_factor=cfg.SOLVER.LR_SCHEDULER.DIV_FACTOR
        )
