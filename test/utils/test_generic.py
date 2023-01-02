#!/usr/bin/env python3

import unittest

import torch

from linear_operator.test.base_test_case import BaseTestCase
from linear_operator.utils.generic import _to_helper


class TestGenericUtils(BaseTestCase, unittest.TestCase):
    def test_to_helper(self):
        device, dtype = _to_helper(device=torch.device("cpu"))
        self.assertEqual(device, torch.device("cpu"))
        self.assertIsNone(dtype)

        device, dtype = _to_helper(torch.device("cpu"))
        self.assertEqual(device, torch.device("cpu"))
        self.assertIsNone(dtype)

        device, dtype = _to_helper(dtype=torch.double)
        self.assertEqual(dtype, torch.double)
        self.assertIsNone(device)

        device, dtype = _to_helper(torch.double)
        self.assertEqual(dtype, torch.double)
        self.assertIsNone(device)

        device, dtype = _to_helper(torch.rand(1, dtype=torch.double))
        self.assertEqual(dtype, torch.double)
        self.assertEqual(device, torch.device("cpu"))

        with self.assertRaisesRegex(RuntimeError, "Attempted to cast"):
            _to_helper(torch.rand(1, dtype=torch.double), dtype=torch.float)
