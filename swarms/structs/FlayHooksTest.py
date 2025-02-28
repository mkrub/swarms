
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.v4core.src.interfaces.IHooks import IHooks
from pytypes.lib.v4core.src.interfaces.IPoolManager import IPoolManager
from pytypes.lib.v4core.src.libraries.Hooks import Hooks
from pytypes.lib.v4periphery.src.base.hooks.BaseHook import BaseHook
from pytypes.src.contracts.bidwall.BidWall import BidWall
from pytypes.src.contracts.hooks.InternalSwapPool import InternalSwapPool

from pytypes.lib.v4core.src.types.PoolKey import PoolKey



class FlayHooks(InternalSwapPool, BaseHook):
    """
    [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#25)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'uint160', 'name': '_initialSqrtPriceX96', 'type': 'uint160'}, {'internalType': 'address', 'name': '_protocolOwner', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xa2-a\xd6': {'inputs': [], 'name': 'CannotBeInitializedDirectly', 'type': 'error'}, b'\n\x85\xdc)': {'inputs': [], 'name': 'HookNotImplemented', 'type': 'error'}, b' \x83\xcd@': {'inputs': [], 'name': 'InvalidPool', 'type': 'error'}, b'\xa4\n\xfa8': {'inputs': [], 'name': 'LockFailure', 'type': 'error'}, b'\xae\x18!\n': {'inputs': [], 'name': 'NotPoolManager', 'type': 'error'}, b')\xc3\xb7\xee': {'inputs': [], 'name': 'NotSelf', 'type': 'error'}, b'\xc7$\x1ai\xd3f\x0b\xdf\xe5\xf3k\xdc\xca;-\xa1\xfe\x88D6nF\xad\xb5\x8b\xe9Qq\xab\x06e\xad': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'PoolId', 'name': '_poolId', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': '_donateAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_creatorAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_bidWallAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_governanceAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_protocolAmount', 'type': 'uint256'}], 'name': 'PoolFeesDistributed', 'type': 'event'}, b"\xa2E\xa9\xa3\x8e\x88w\xad\xd8/\n\x82\xc1>\x06*\xb3\xdf\x16\xa2a!\x97}\xdc\xca\x88'\xd4li\n": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'PoolId', 'name': '_poolId', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount1', 'type': 'uint256'}], 'name': 'PoolFeesReceived', 'type': 'event'}, b'\xce\x97\xca\xf4\xfd\x02\x95\xde\x95D\xb5+K\x9ey\xfe4\xc3p\xbe\xbbo\xb7\x1b\xc5\xba\xae\x9ap yh': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'PoolId', 'name': '_poolId', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bool', 'name': 'zeroForOne', 'type': 'bool'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount1', 'type': 'uint256'}], 'name': 'PoolFeesSwapped', 'type': 'event'}, b'\x12\xa5\xd5\xbf': {'inputs': [], 'name': 'BASE_SWAP_FEE', 'outputs': [{'internalType': 'uint24', 'name': '', 'type': 'uint24'}], 'stateMutability': 'view', 'type': 'function'}, b')\x9dS.': {'inputs': [], 'name': 'MIN_DISTRIBUTE_THRESHOLD', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xaa\xce\x00\x8e': {'inputs': [], 'name': '_poolManager', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9f\x06>\xfc': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'components': [{'internalType': 'int24', 'name': 'tickLower', 'type': 'int24'}, {'internalType': 'int24', 'name': 'tickUpper', 'type': 'int24'}, {'internalType': 'int256', 'name': 'liquidityDelta', 'type': 'int256'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'internalType': 'struct IPoolManager.ModifyLiquidityParams', 'name': '', 'type': 'tuple'}, {'internalType': 'BalanceDelta', 'name': '', 'type': 'int256'}, {'internalType': 'BalanceDelta', 'name': '', 'type': 'int256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'afterAddLiquidity', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}, {'internalType': 'BalanceDelta', 'name': '', 'type': 'int256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe1\xb4\xafi': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'afterDonate', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'o\xe7\xe6\xeb': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'internalType': 'uint160', 'name': '', 'type': 'uint160'}, {'internalType': 'int24', 'name': '', 'type': 'int24'}], 'name': 'afterInitialize', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'l+\xbe~': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'components': [{'internalType': 'int24', 'name': 'tickLower', 'type': 'int24'}, {'internalType': 'int24', 'name': 'tickUpper', 'type': 'int24'}, {'internalType': 'int256', 'name': 'liquidityDelta', 'type': 'int256'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'internalType': 'struct IPoolManager.ModifyLiquidityParams', 'name': '', 'type': 'tuple'}, {'internalType': 'BalanceDelta', 'name': '', 'type': 'int256'}, {'internalType': 'BalanceDelta', 'name': '', 'type': 'int256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'afterRemoveLiquidity', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}, {'internalType': 'BalanceDelta', 'name': '', 'type': 'int256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb4{/\xb1': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '_key', 'type': 'tuple'}, {'components': [{'internalType': 'bool', 'name': 'zeroForOne', 'type': 'bool'}, {'internalType': 'int256', 'name': 'amountSpecified', 'type': 'int256'}, {'internalType': 'uint160', 'name': 'sqrtPriceLimitX96', 'type': 'uint160'}], 'internalType': 'struct IPoolManager.SwapParams', 'name': '_params', 'type': 'tuple'}, {'internalType': 'BalanceDelta', 'name': '_delta', 'type': 'int256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'afterSwap', 'outputs': [{'internalType': 'bytes4', 'name': 'selector_', 'type': 'bytes4'}, {'internalType': 'int128', 'name': 'hookDeltaUnspecified_', 'type': 'int128'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'%\x99\x82\xe5': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'components': [{'internalType': 'int24', 'name': 'tickLower', 'type': 'int24'}, {'internalType': 'int24', 'name': 'tickUpper', 'type': 'int24'}, {'internalType': 'int256', 'name': 'liquidityDelta', 'type': 'int256'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'internalType': 'struct IPoolManager.ModifyLiquidityParams', 'name': '', 'type': 'tuple'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'beforeAddLiquidity', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb6\xa8\xb0\xfa': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'beforeDonate', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xdc\x985N': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'internalType': 'uint160', 'name': '', 'type': 'uint160'}], 'name': 'beforeInitialize', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'view', 'type': 'function'}, b'!\xd0\xeep': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '', 'type': 'tuple'}, {'components': [{'internalType': 'int24', 'name': 'tickLower', 'type': 'int24'}, {'internalType': 'int24', 'name': 'tickUpper', 'type': 'int24'}, {'internalType': 'int256', 'name': 'liquidityDelta', 'type': 'int256'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'internalType': 'struct IPoolManager.ModifyLiquidityParams', 'name': '', 'type': 'tuple'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'beforeRemoveLiquidity', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'W^$\xb4': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '_key', 'type': 'tuple'}, {'components': [{'internalType': 'bool', 'name': 'zeroForOne', 'type': 'bool'}, {'internalType': 'int256', 'name': 'amountSpecified', 'type': 'int256'}, {'internalType': 'uint160', 'name': 'sqrtPriceLimitX96', 'type': 'uint160'}], 'internalType': 'struct IPoolManager.SwapParams', 'name': '_params', 'type': 'tuple'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'beforeSwap', 'outputs': [{'internalType': 'bytes4', 'name': 'selector_', 'type': 'bytes4'}, {'internalType': 'BeforeSwapDelta', 'name': 'beforeSwapDelta_', 'type': 'int256'}, {'internalType': 'uint24', 'name': '', 'type': 'uint24'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xba>i\xb7': {'inputs': [], 'name': 'bidWall', 'outputs': [{'internalType': 'contract BidWall', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'<7\x10\x96': {'inputs': [], 'name': 'flayNativePoolKey', 'outputs': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x19\xcc\xa5\xc6': {'inputs': [], 'name': 'flayToken', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc4\xe83\xce': {'inputs': [], 'name': 'getHookPermissions', 'outputs': [{'components': [{'internalType': 'bool', 'name': 'beforeInitialize', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterInitialize', 'type': 'bool'}, {'internalType': 'bool', 'name': 'beforeAddLiquidity', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterAddLiquidity', 'type': 'bool'}, {'internalType': 'bool', 'name': 'beforeRemoveLiquidity', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterRemoveLiquidity', 'type': 'bool'}, {'internalType': 'bool', 'name': 'beforeSwap', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterSwap', 'type': 'bool'}, {'internalType': 'bool', 'name': 'beforeDonate', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterDonate', 'type': 'bool'}, {'internalType': 'bool', 'name': 'beforeSwapReturnDelta', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterSwapReturnDelta', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterAddLiquidityReturnDelta', 'type': 'bool'}, {'internalType': 'bool', 'name': 'afterRemoveLiquidityReturnDelta', 'type': 'bool'}], 'internalType': 'struct Hooks.Permissions', 'name': '', 'type': 'tuple'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xe1u\x8b\xd8': {'inputs': [], 'name': 'nativeToken', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xdd\xb4u\xd5': {'inputs': [{'components': [{'internalType': 'Currency', 'name': 'currency0', 'type': 'address'}, {'internalType': 'Currency', 'name': 'currency1', 'type': 'address'}, {'internalType': 'uint24', 'name': 'fee', 'type': 'uint24'}, {'internalType': 'int24', 'name': 'tickSpacing', 'type': 'int24'}, {'internalType': 'contract IHooks', 'name': 'hooks', 'type': 'address'}], 'internalType': 'struct PoolKey', 'name': '_poolKey', 'type': 'tuple'}], 'name': 'poolFees', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}], 'internalType': 'struct InternalSwapPool.ClaimableFees', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, b'\xdcL\x90\xd3': {'inputs': [], 'name': 'poolManager', 'outputs': [{'internalType': 'contract IPoolManager', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91\xddsF': {'inputs': [{'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'unlockCallback', 'outputs': [{'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":13852,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"_poolFees","offset":0,"slot":0,"type":"t_mapping(t_userDefinedValueType(PoolId)7032,t_struct(ClaimableFees)13845_storage)"},{"astId":7966,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"flayNativePoolKey","offset":0,"slot":1,"type":"t_struct(PoolKey)7078_storage"},{"astId":7969,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"_beforeSwapTick","offset":0,"slot":4,"type":"t_int24"}],"types":{"t_contract(IHooks)1687":{"encoding":"inplace","label":"contract IHooks","numberOfBytes":20},"t_int24":{"encoding":"inplace","label":"int24","numberOfBytes":3},"t_mapping(t_userDefinedValueType(PoolId)7032,t_struct(ClaimableFees)13845_storage)":{"encoding":"mapping","label":"mapping(PoolId => struct InternalSwapPool.ClaimableFees)","numberOfBytes":32,"key":"t_userDefinedValueType(PoolId)7032","value":"t_struct(ClaimableFees)13845_storage"},"t_struct(ClaimableFees)13845_storage":{"encoding":"inplace","label":"struct InternalSwapPool.ClaimableFees","numberOfBytes":64,"members":[{"astId":13842,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"amount0","offset":0,"slot":0,"type":"t_uint256"},{"astId":13844,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"amount1","offset":0,"slot":1,"type":"t_uint256"}]},"t_struct(PoolKey)7078_storage":{"encoding":"inplace","label":"struct PoolKey","numberOfBytes":96,"members":[{"astId":7063,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"currency0","offset":0,"slot":0,"type":"t_userDefinedValueType(Currency)6732"},{"astId":7067,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"currency1","offset":0,"slot":1,"type":"t_userDefinedValueType(Currency)6732"},{"astId":7070,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"fee","offset":20,"slot":1,"type":"t_uint24"},{"astId":7073,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"tickSpacing","offset":23,"slot":1,"type":"t_int24"},{"astId":7077,"contract":"src/contracts/FlayHooks.sol:FlayHooks","label":"hooks","offset":0,"slot":2,"type":"t_contract(IHooks)1687"}]},"t_uint24":{"encoding":"inplace","label":"uint24","numberOfBytes":3},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_userDefinedValueType(Currency)6732":{"encoding":"inplace","label":"Currency","numberOfBytes":20},"t_userDefinedValueType(PoolId)7032":{"encoding":"inplace","label":"PoolId","numberOfBytes":32}}}
    _creation_code = "60c060405234801561000f575f5ffd5b506040516150ac3803806150ac83398101604081905261002e916104fd565b73498581ff718922c3f8e6a244956af099b2652b2b608081905261005130610284565b506f0d564d5be76f7f0d28fe52605afc7cf873498581ff718922c3f8e6a244956af099b2652b2b82604051610085906104dc565b6001600160a01b03938416815291831660208301529091166040820152606001604051809103905ff0801580156100be573d5f5f3e3d5ffd5b506001600160a01b031660a081905260405163095ea7b360e01b815260048101919091525f1960248201526f0d564d5be76f7f0d28fe52605afc7cf89063095ea7b3906044016020604051808303815f875af1158015610120573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906101449190610535565b506040805160a080820183526f0d564d5be76f7f0d28fe52605afc7cf880835273f1a7000000950c7ad8aff13118bb7ab561a448ee602084018190525f84860152603c6060850152306080948501819052600180546001600160a01b0319908116851790915560028054773c000000f1a7000000950c7ad8aff13118bb7ab561a448ee6001600160d01b0319909116178082556003805490931684179092559551965163313b65df60e11b8152600481019490945260248401929092529281901c62ffffff16604483015260b81c90920b606483015260848201526001600160a01b0384811660a483015290911690636276cbbe9060c4016020604051808303815f875af1158015610258573d5f5f3e3d5ffd5b505050506040513d601f19601f8201168201806040525081019061027c919061055b565b50505061057b565b6103748161036f604080516101c0810182525f80825260208201819052918101829052606081018290526080810182905260a0810182905260c0810182905260e08101829052610100810182905261012081018290526101408101829052610160810182905261018081018290526101a081019190915250604080516101c08101825260018082525f60208301819052928201839052606082018390526080820183905260a0820183905260c0820181905260e0820181905261010082018390526101208201839052610140820181905261016082015261018081018290526101a081019190915290565b610377565b50565b805115156120008316151514158061039b5750602081015115156110008316151514155b806103b25750604081015115156108008316151514155b806103c95750606081015115156104008316151514155b806103e05750608081015115156102008316151514155b806103f7575060a081015115156101008316151514155b8061040d575060c0810151151560808316151514155b80610423575060e0810151151560408316151514155b8061043a5750610100810151151560208316151514155b806104515750610120810151151560108316151514155b806104685750610140810151151560088316151514155b8061047f5750610160810151151560048316151514155b806104965750610180810151151560028316151514155b806104ad57506101a0810151151560018316151514155b156104c3576104c3630732d7b560e51b836104c7565b5050565b815f526001600160a01b03811660045260245ffd5b6128608061284c83390190565b6001600160a01b0381168114610374575f5ffd5b5f5f6040838503121561050e575f5ffd5b8251610519816104e9565b602084015190925061052a816104e9565b809150509250929050565b5f60208284031215610545575f5ffd5b81518015158114610554575f5ffd5b9392505050565b5f6020828403121561056b575f5ffd5b81518060020b8114610554575f5ffd5b60805160a0516122786105d45f395f81816103500152610f0d01525f818161046b0152818161050d015281816105520152818161068501528181610707015281816107650152818161083a0152610ca501526122785ff3fe608060405234801561000f575f5ffd5b5060043610610132575f3560e01c80639f063efc116100b4578063c4e833ce11610079578063c4e833ce14610372578063dc4c90d314610466578063dc98354e1461048d578063ddb475d5146104a0578063e1758bd8146104ce578063e1b4af691461033d575f5ffd5b80639f063efc1461028b578063aace008e146102ec578063b47b2fb114610307578063b6a8b0fa1461033d578063ba3e69b71461034b575f5ffd5b80633c371096116100fa5780633c371096146101d2578063575e24b41461024d5780636c2bbe7e1461028b5780636fe7e6eb146102be57806391dd7346146102cc575f5ffd5b806312a5d5bf1461013657806319cca5c61461015757806321d0ee701461018a578063259982e51461018a578063299d532e146101b6575b5f5ffd5b61013e606481565b60405162ffffff90911681526020015b60405180910390f35b61017273f1a7000000950c7ad8aff13118bb7ab561a448ee81565b6040516001600160a01b03909116815260200161014e565b61019d610198366004611a3b565b6104e5565b6040516001600160e01b0319909116815260200161014e565b6101c466038d7ea4c6800081565b60405190815260200161014e565b6001546002805460035461020d936001600160a01b03908116938382169362ffffff600160a01b82041693600160b81b90910490910b911685565b604080516001600160a01b039687168152948616602086015262ffffff9093169284019290925260020b606083015291909116608082015260a00161014e565b61026061025b366004611b36565b6104ff565b604080516001600160e01b03199094168452602084019290925262ffffff169082015260600161014e565b61029e610299366004611b90565b6106df565b604080516001600160e01b0319909316835260208301919091520161014e565b61019d610198366004611c2c565b6102df6102da366004611c83565b6106fa565b60405161014e9190611cc2565b61017273498581ff718922c3f8e6a244956af099b2652b2b81565b61031a610315366004611cf7565b610758565b604080516001600160e01b03199093168352600f9190910b60208301520161014e565b61019d610198366004611d82565b6101727f000000000000000000000000000000000000000000000000000000000000000081565b610459604080516101c0810182525f80825260208201819052918101829052606081018290526080810182905260a0810182905260c0810182905260e08101829052610100810182905261012081018290526101408101829052610160810182905261018081018290526101a081019190915250604080516101c08101825260018082525f60208301819052928201839052606082018390526080820183905260a0820183905260c0820181905260e0820181905261010082018390526101208201839052610140820181905261016082015261018081018290526101a081019190915290565b60405161014e9190611ddc565b6101727f000000000000000000000000000000000000000000000000000000000000000081565b61019d61049b366004611efd565b61082e565b6104b36104ae366004611f44565b610891565b6040805182518152602092830151928101929092520161014e565b6101726f0d564d5be76f7f0d28fe52605afc7cf881565b5f604051630a85dc2960e01b815260040160405180910390fd5b5f8080336001600160a01b037f0000000000000000000000000000000000000000000000000000000000000000161461054b5760405163570c108560e11b815260040160405180910390fd5b5f5f61057a7f00000000000000000000000000000000000000000000000000000000000000008a8a60016108e3565b90925090506105898183612001565b1561065f575f5f896020015112156105d1576105cc6105a784610bc5565b6105b084610bc5565b6105b990612014565b6001600160801b031660809190911b1790565b6105ef565b6105ef6105dd83610bc5565b6105e690612014565b6105b985610bc5565b90505f6106068b8b61060185600f0b90565b610be5565b905061065a6106158360801d90565b61061f8860801d90565b6106299190612038565b61063283610bc5565b61063c85600f0b90565b6106468a600f0b90565b6106509190612038565b6105b99190612038565b955050505b6106ab61067b610674368c90038c018c611f44565b60a0902090565b6001600160a01b037f00000000000000000000000000000000000000000000000000000000000000001690610d70565b50506004805462ffffff191662ffffff92909216919091179055506315d7892d60e21b9a9399509197509195505050505050565b5f5f604051630a85dc2960e01b815260040160405180910390fd5b6060336001600160a01b037f000000000000000000000000000000000000000000000000000000000000000016146107455760405163570c108560e11b815260040160405180910390fd5b61074f8383610e22565b90505b92915050565b5f80336001600160a01b037f000000000000000000000000000000000000000000000000000000000000000016146107a35760405163570c108560e11b815260040160405180910390fd5b5f6107b1602088018861206e565b15155f602089013512146107ce576107c98660801d90565b6107d8565b6107d886600f0b90565b90505f6107f4896107ee368b90038b018b612089565b84610be5565b905061080d610808368b90038b018b611f44565b610ebb565b61081681610bc5565b63b47b2fb160e01b9b909a5098505050505050505050565b5f336001600160a01b037f000000000000000000000000000000000000000000000000000000000000000016146108785760405163570c108560e11b815260040160405180910390fd5b604051635116b0eb60e11b815260040160405180910390fd5b604080518082019091525f80825260208201525f5f6108b18460a0902090565b81526020019081526020015f206040518060400160405290815f82015481526020016001820154815250509050919050565b5f80806108f861067436889003880188611f44565b5f818152602081905260408120600181015492935091900361091b575050610bbc565b855115158515151461092e575050610bbc565b5f6109426001600160a01b038a1684610d70565b50505090505f8760200151126109ae575f826001015488602001511161096c578760200151610972565b82600101545b90506109a0828960400151610999878e6001600160a01b0316610fce90919063ffffffff16565b845f61105a565b509097509550610a4f915050565b610a1581885f01516109cf576109ca6401000276a360016120a3565b6109ee565b6109ee600173fffd8963efd1fc6a506488495d951d5263988d266120c2565b610a016001600160a01b038d1687610fce565b8a60200151610a0f906120e1565b5f61105a565b5060018501549097509095508511159050610a4f5783858360010154610a3b91906120fb565b610a459190612126565b9450816001015493505b84158015610a5b575083155b15610a6857505050610bbc565b84825f015f828254610a7a9190612001565b9250508190555083826001015f828254610a949190612145565b90915550506001600160a01b038916630b0d9c098715610ac057610abb60208b018b612158565b610ad0565b610ad060408b0160208c01612158565b6040516001600160e01b031960e084901b1681526001600160a01b039091166004820152306024820152604481018890526064015f604051808303815f87803b158015610b1b575f5ffd5b505af1158015610b2d573d5f5f3e3d5ffd5b50505050610b728930865f8a15610b5357610b4e60408e0160208f01612158565b610b60565b610b6060208e018e612158565b6001600160a01b0316939291906111bd565b865160408051911515825260208201879052810185905283907fce97caf4fd0295de9544b52b4b9e79fe34c370bebb6fb71bc5baae9a702079689060600160405180910390a25050505b94509492505050565b5f6001607f1b8210610be157610be16393dafdf160e01b611488565b5090565b5f5f835f015115155f856020015112151514610c0d57610c086020860186612158565b610c1d565b610c1d6040860160208701612158565b90505f5f84600f0b12610c305783610c39565b610c3984612014565b9050806001600160801b03165f03610c55575f92505050610d69565b612710610c63606483612173565b6001600160801b0316610c769190612126565b604051630b0d9c0960e01b81526001600160a01b038481166004830152306024830152604482018390529194507f000000000000000000000000000000000000000000000000000000000000000090911690630b0d9c09906064015f604051808303815f87803b158015610ce8575f5ffd5b505af1158015610cfa573d5f5f3e3d5ffd5b50505050610d6686803603810190610d129190611f44565b6001600160a01b0384166f0d564d5be76f7f0d28fe52605afc7cf814610d38575f610d3a565b845b6001600160a01b0385166f0d564d5be76f7f0d28fe52605afc7cf814610d605785611490565b5f611490565b50505b9392505050565b5f5f5f5f5f610d7e8661151c565b604051631e2eaeaf60e01b8152600481018290529091505f906001600160a01b03891690631e2eaeaf90602401602060405180830381865afa158015610dc6573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610dea9190612195565b90506001600160a01b03811695508060a01c60020b945062ffffff8160b81c16935062ffffff8160d01c169250505092959194509250565b60605f5f306001600160a01b03168585604051610e409291906121ac565b5f604051808303815f865af19150503d805f8114610e79576040519150601f19603f3d011682016040523d82523d5f602084013e610e7e565b606091505b50915091508115610e925791506107529050565b80515f03610eb3576040516314815f4760e31b815260040160405180910390fd5b805160208201fd5b60a081205f8181526020819052604090205466038d7ea4c68000811015610ee157505050565b5f828152602081905260408082209190915560048054915163088a80c760e01b81526001600160a01b037f0000000000000000000000000000000000000000000000000000000000000000169263088a80c792610f4c928892879260029190910b91600191016121bb565b5f604051808303815f87803b158015610f63575f5ffd5b505af1158015610f75573d5f5f3e3d5ffd5b5050604080518481525f6020820181905281830186905260608201819052608082015290518593507fc7241a69d3660bdfe5f36bdcca3b2da1fe8844366e46adb58be95171ab0665ad92509081900360a00190a2505050565b5f5f610fd98361151c565b90505f610fe7600383612001565b604051631e2eaeaf60e01b8152600481018290529091506001600160a01b03861690631e2eaeaf90602401602060405180830381865afa15801561102d573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906110519190612195565b95945050505050565b5f80808062ffffff85166001600160a01b03808a16908b1610158288128015611130575f6110938a5f0385620f424003620f4240611558565b9050826110ac576110a78d8d8d60016115f4565b6110b9565b6110b98c8e8d6001611640565b96508681106110ed578b9750620f424084146110e4576110df878586620f424003611705565b6110e6565b865b9450611106565b8096506110fc8d8c8386611735565b9750868a5f030394505b8261111c576111178d898d5f611640565b611128565b611128888e8d5f6115f4565b9550506111ae565b81611146576111418c8c8c5f611640565b611152565b6111528b8d8c5f6115f4565b9450848910611163578a9650611175565b8894506111728c8b8785611783565b96505b8161118c576111878c888c60016115f4565b611199565b611199878d8c6001611640565b95506111ab868485620f424003611705565b93505b50505095509550955095915050565b801561125157836001600160a01b031663f5298aca846111ec886001600160a01b03166001600160a01b031690565b6040516001600160e01b031960e085901b1681526001600160a01b0390921660048301526024820152604481018590526064015f604051808303815f87803b158015611236575f5ffd5b505af1158015611248573d5f5f3e3d5ffd5b50505050611481565b6001600160a01b0385166112c857836001600160a01b03166311da60b4836040518263ffffffff1660e01b815260040160206040518083038185885af115801561129d573d5f5f3e3d5ffd5b50505050506040513d601f19601f820116820180604052508101906112c29190612195565b50611481565b604051632961046560e21b81526001600160a01b03868116600483015285169063a5841194906024015f604051808303815f87803b158015611308575f5ffd5b505af115801561131a573d5f5f3e3d5ffd5b505050506001600160a01b03831630146113ac576040516323b872dd60e01b81526001600160a01b0384811660048301528581166024830152604482018490528616906323b872dd906064016020604051808303815f875af1158015611382573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906113a69190612227565b5061141e565b60405163a9059cbb60e01b81526001600160a01b0385811660048301526024820184905286169063a9059cbb906044016020604051808303815f875af11580156113f8573d5f5f3e3d5ffd5b505050506040513d601f19601f8201168201806040525081019061141c9190612227565b505b836001600160a01b03166311da60b46040518163ffffffff1660e01b81526004016020604051808303815f875af115801561145b573d5f5f3e3d5ffd5b505050506040513d601f19601f8201168201806040525081019061147f9190612195565b505b5050505050565b805f5260045ffd5b60a083205f81815260208190526040812080548592906114b1908490612001565b90915550505f81815260208190526040812060010180548492906114d6908490612001565b9091555050604080518481526020810184905282917fa245a9a38e8877add82f0a82c13e062ab3df16a26121977ddcca8827d46c690a910160405180910390a250505050565b6040515f9061153b908390600690602001918252602082015260400190565b604051602081830303815290604052805190602001209050919050565b5f838302815f1985870982811083820303915050808411611577575f5ffd5b805f0361158957508290049050610d69565b5f848688095f868103871696879004966002600389028118808a02820302808a02820302808a02820302808a02820302808a02820302808a02909103029181900381900460010186841190950394909402919094039290920491909117919091029150509392505050565b5f6001600160a01b038481169086160360ff81901d90810118600160601b6001600160801b038516611627818484611558565b9350845f83858409111684019350505050949350505050565b5f836001600160a01b0316856001600160a01b0316111561165f579293925b6001600160a01b0385166116795762bfc9215f526004601cfd5b600160601b600160e01b03606084901b166001600160a01b0386860316836116cc57866001600160a01b03166116b98383896001600160a01b0316611558565b816116c6576116c6612112565b046116f8565b6116f86116e38383896001600160a01b0316611705565b886001600160a01b0316808204910615150190565b925050505b949350505050565b5f611711848484611558565b9050818061172157611721612112565b83850915610d695760010180610d69575f5ffd5b5f6001600160801b038416156001600160a01b03861615171561175f57634f2461b85f526004601cfd5b816117765761177185858560016117c6565b611051565b61105185858560016118b1565b5f6001600160801b038416156001600160a01b0386161517156117ad57634f2461b85f526004601cfd5b816117be576117718585855f6118b1565b6110518585855f5b5f8115611836575f6001600160a01b038411156117fa576117f584600160601b876001600160801b0316611558565b611811565b6118116001600160801b038616606086901b612126565b905061182e611829826001600160a01b038916612001565b611993565b9150506116fd565b5f6001600160a01b038411156118635761185e84600160601b876001600160801b0316611705565b611880565b611880606085901b6001600160801b038716808204910615150190565b9050806001600160a01b0387161161189f57634323a5555f526004601cfd5b6001600160a01b0386160390506116fd565b5f825f036118c05750836116fd565b600160601b600160e01b03606085901b168215611952576001600160a01b038616848102908582816118f4576118f4612112565b0403611924578181018281106119225761191883896001600160a01b031683611705565b93505050506116fd565b505b5061182e818561193d6001600160a01b038a1683612126565b6119479190612001565b808204910615150190565b6001600160a01b0386168481029085820414818311166119795763f5c787f15f526004601cfd5b808203611918611829846001600160a01b038b1684611705565b806001600160a01b03811681146119b4576119b46393dafdf160e01b611488565b919050565b6001600160a01b03811681146119cd575f5ffd5b50565b5f60a082840312156119e0575f5ffd5b50919050565b5f608082840312156119e0575f5ffd5b5f5f83601f840112611a06575f5ffd5b50813567ffffffffffffffff811115611a1d575f5ffd5b602083019150836020828501011115611a34575f5ffd5b9250929050565b5f5f5f5f5f6101608688031215611a50575f5ffd5b8535611a5b816119b9565b9450611a6a87602088016119d0565b9350611a798760c088016119e6565b925061014086013567ffffffffffffffff811115611a95575f5ffd5b611aa1888289016119f6565b969995985093965092949392505050565b80151581146119cd575f5ffd5b5f60608284031215611acf575f5ffd5b6040516060810167ffffffffffffffff81118282101715611afe57634e487b7160e01b5f52604160045260245ffd5b6040529050808235611b0f81611ab2565b8152602083810135908201526040830135611b29816119b9565b6040919091015292915050565b5f5f5f5f5f6101408688031215611b4b575f5ffd5b8535611b56816119b9565b9450611b6587602088016119d0565b9350611b748760c08801611abf565b925061012086013567ffffffffffffffff811115611a95575f5ffd5b5f5f5f5f5f5f5f6101a0888a031215611ba7575f5ffd5b8735611bb2816119b9565b9650611bc18960208a016119d0565b9550611bd08960c08a016119e6565b94506101408801359350610160880135925061018088013567ffffffffffffffff811115611bfc575f5ffd5b611c088a828b016119f6565b989b979a50959850939692959293505050565b8035600281900b81146119b4575f5ffd5b5f5f5f5f6101008587031215611c40575f5ffd5b8435611c4b816119b9565b9350611c5a86602087016119d0565b925060c0850135611c6a816119b9565b9150611c7860e08601611c1b565b905092959194509250565b5f5f60208385031215611c94575f5ffd5b823567ffffffffffffffff811115611caa575f5ffd5b611cb6858286016119f6565b90969095509350505050565b602081525f82518060208401528060208501604085015e5f604082850101526040601f19601f83011684010191505092915050565b5f5f5f5f5f5f868803610160811215611d0e575f5ffd5b8735611d19816119b9565b9650611d288960208a016119d0565b9550606060bf1982011215611d3b575f5ffd5b5060c087019350610120870135925061014087013567ffffffffffffffff811115611d64575f5ffd5b611d7089828a016119f6565b979a9699509497509295939492505050565b5f5f5f5f5f5f6101208789031215611d98575f5ffd5b8635611da3816119b9565b9550611db288602089016119d0565b945060c0870135935060e0870135925061010087013567ffffffffffffffff811115611d64575f5ffd5b8151151581526101c081016020830151611dfa602084018215159052565b506040830151611e0e604084018215159052565b506060830151611e22606084018215159052565b506080830151611e36608084018215159052565b5060a0830151611e4a60a084018215159052565b5060c0830151611e5e60c084018215159052565b5060e0830151611e7260e084018215159052565b50610100830151611e8861010084018215159052565b50610120830151611e9e61012084018215159052565b50610140830151611eb461014084018215159052565b50610160830151611eca61016084018215159052565b50610180830151611ee061018084018215159052565b506101a0830151611ef66101a084018215159052565b5092915050565b5f5f5f60e08486031215611f0f575f5ffd5b8335611f1a816119b9565b9250611f2985602086016119d0565b915060c0840135611f39816119b9565b809150509250925092565b5f60a0828403128015611f55575f5ffd5b5060405160a0810167ffffffffffffffff81118282101715611f8557634e487b7160e01b5f52604160045260245ffd5b6040528235611f93816119b9565b81526020830135611fa3816119b9565b6020820152604083013562ffffff81168114611fbd575f5ffd5b6040820152611fce60608401611c1b565b60608201526080830135611fe1816119b9565b60808201529392505050565b634e487b7160e01b5f52601160045260245ffd5b8082018082111561075257610752611fed565b5f81600f0b60016001607f1b0319810361203057612030611fed565b5f0392915050565b600f81810b9083900b0160016001607f1b0381136f7fffffffffffffffffffffffffffffff198212171561075257610752611fed565b5f6020828403121561207e575f5ffd5b8135610d6981611ab2565b5f60608284031215612099575f5ffd5b61074f8383611abf565b6001600160a01b03818116838216019081111561075257610752611fed565b6001600160a01b03828116828216039081111561075257610752611fed565b5f600160ff1b82016120f5576120f5611fed565b505f0390565b808202811582820484141761075257610752611fed565b634e487b7160e01b5f52601260045260245ffd5b5f8261214057634e487b7160e01b5f52601260045260245ffd5b500490565b8181038181111561075257610752611fed565b5f60208284031215612168575f5ffd5b8135610d69816119b9565b6001600160801b038181168382160290811690818114611ef657611ef6611fed565b5f602082840312156121a5575f5ffd5b5051919050565b818382375f9101908152919050565b84516001600160a01b03908116825260208087015182169083015260408087015162ffffff169083015260608087015160020b908301526080808701519091169082015260a08101849052610100810161221a60c083018560020b9052565b82151560e0830152611051565b5f60208284031215612237575f5ffd5b8151610d6981611ab256fea2646970667358221220755b59a28236e3ba4e3cac7d7171ed0547386ea1bca9f5d195827330c5a2e96664736f6c634300081c003360e060405234801561000f575f5ffd5b5060405161286038038061286083398101604081905261002e91610109565b3360a0526001600160a01b0383811660c052821660805267016345785d8a00005f8190556040519081527ff33554d7210318fe10b4d834a6233a2fd789ea1db37278b7e27f433b9e8659c79060200160405180910390a161008e81610096565b505050610149565b638b78c6d8198054156100b057630dc149f05f526004601cfd5b6001600160a01b03909116801560ff1b8117909155805f7f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e08180a350565b80516001600160a01b0381168114610104575f5ffd5b919050565b5f5f5f6060848603121561011b575f5ffd5b610124846100ee565b9250610132602085016100ee565b9150610140604085016100ee565b90509250925092565b60805160a05160c05161265361020d5f395f818161034b015281816105540152818161064501528181610a6201528181610b0901528181610be601528181610c7e0152610e0601525f818161018c015281816103dd0152818161052501528181610a2001528181610baf01528181610f0c015261123601525f8181610318015281816105e101528181610963015281816109ad01528181611037015281816116f4015281816117ce01528181611839015281816118fa015261196801526126535ff3fe6080604052600436106100fa575f3560e01c80638da5cb5b11610092578063dc4c90d311610062578063dc4c90d314610307578063e1758bd81461033a578063f04e283e1461036d578063f2fde38b14610380578063fee81cf414610393575f5ffd5b80638da5cb5b14610277578063957d1fe11461028f578063ad49d66e146102c9578063cfbc79fe146102e8575f5ffd5b8063715018a6116100cd578063715018a614610173578063791b98bc1461017b578063870b9c17146101c65780638cebd942146101e5575f5ffd5b8063088a80c7146100fe578063256929621461011f5780634e944d571461012757806354d1f13d1461016b575b5f5ffd5b348015610109575f5ffd5b5061011d61011836600461222d565b6103d2565b005b61011d6107f4565b348015610132575f5ffd5b5061015661014136600461227b565b5f9081526001602052604090205460ff161590565b60405190151581526020015b60405180910390f35b61011d610841565b61011d61087a565b348015610186575f5ffd5b506101ae7f000000000000000000000000000000000000000000000000000000000000000081565b6040516001600160a01b039091168152602001610162565b3480156101d1575f5ffd5b5061011d6101e036600461227b565b61088d565b3480156101f0575f5ffd5b506102416101ff36600461227b565b600160208190525f918252604090912080549181015460029182015460ff80851694610100810490911693620100008204810b93600160281b909204900b9186565b6040805196151587529415156020870152600293840b94860194909452910b6060840152608083015260a082015260c001610162565b348015610282575f5ffd5b50638b78c6d819546101ae565b34801561029a575f5ffd5b506102ae6102a936600461227b565b6108cf565b60408051938452602084019290925290820152606001610162565b3480156102d4575f5ffd5b5061011d6102e3366004612292565b610a15565b3480156102f3575f5ffd5b5061011d6103023660046122ac565b610e00565b348015610312575f5ffd5b506101ae7f000000000000000000000000000000000000000000000000000000000000000081565b348015610345575f5ffd5b506101ae7f000000000000000000000000000000000000000000000000000000000000000081565b61011d61037b3660046122e2565b610fb9565b61011d61038e3660046122e2565b610ff6565b34801561039e575f5ffd5b506103c46103ad3660046122e2565b63389a75e1600c9081525f91909152602090205490565b604051908152602001610162565b336001600160a01b037f0000000000000000000000000000000000000000000000000000000000000000161461041b5760405163041fb8cb60e31b815260040160405180910390fd5b82156107ee5760a084205f81815260016020526040812060028101805491928792610447908490612311565b9250508190555084816001015f8282546104619190612311565b9091555050600181015460405183917fa5f00d866fe48379f7d8a625ccea2f92572b5cbd3f234591dfa4c7f845836fd0916104a491898252602082015260400190565b60405180910390a25f54816001015410156104c05750506107ee565b6001810180545f9182905582549091908190610100900460ff16156105c5578354610503908a908890620100008104600290810b91600160281b9004900b61101c565b909250905081156105c05760405163a9059cbb60e01b81526001600160a01b037f000000000000000000000000000000000000000000000000000000000000000081166004830152602482018490527f0000000000000000000000000000000000000000000000000000000000000000169063a9059cbb906044016020604051808303815f875af115801561059a573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906105be9190612324565b505b6105d3565b835461ff0019166101001784555b5f6106076001600160a01b037f000000000000000000000000000000000000000000000000000000000000000016876110d4565b50509150508760020b8160020b13151587151503610623578097505b6106388a888a6106338888612311565b611186565b8115610788575f6106698b7f00000000000000000000000000000000000000000000000000000000000000006112bb565b90505f816001600160a01b03166361d027b36040518163ffffffff1660e01b8152600401602060405180830381865afa1580156106a8573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906106cc919061233f565b60405163a9059cbb60e01b81526001600160a01b038083166004830152602482018790529192509083169063a9059cbb906044016020604051808303815f875af115801561071c573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906107409190612324565b50604080516001600160a01b03831681526020810186905289917f6f25beea688da23574729528d9040ac00b2a9f98fe04601175b5bed75222d37b910160405180910390a250505b857fba69105014fb62310aea3b6cd667c51d18201a3c7112e2ead21829195f6fa3fc6107b48686612311565b875460408051928352620100008204600290810b6020850152600160281b90920490910b9082015260600160405180910390a25050505050505b50505050565b5f6202a30067ffffffffffffffff164201905063389a75e1600c52335f52806020600c2055337fdbf36a107da19e49527a7176a1babf963b4b0ff8cde35ee35d6cd8f1f9ac7e1d5f5fa250565b63389a75e1600c52335f525f6020600c2055337ffa7b8eab7da67f412cc9575ed43464468f9bfbae89d1675917346ca6d8fe3c925f5fa2565b6108826112e7565b61088b5f611301565b565b6108956112e7565b5f8190556040518181527ff33554d7210318fe10b4d834a6233a2fd789ea1db37278b7e27f433b9e8659c79060200160405180910390a150565b5f818152600160208181526040808420815160c081018352815460ff808216151583526101008204161515948201859052620100008104600290810b94830194909452600160281b9004830b6060820152938101546080850152015460a08301528291829161094957608001515f93508392509050610a0e565b604081015160608201515f91610999916001600160a01b037f00000000000000000000000000000000000000000000000000000000000000001691899130919066189a591dd85b1b60ca1b611347565b509091505f90506109d36001600160a01b037f000000000000000000000000000000000000000000000000000000000000000016886110d4565b50505090506109fc816109e9856040015161139e565b6109f6866060015161139e565b85611656565b60809094015190965092945091925050505b9193909250565b336001600160a01b037f00000000000000000000000000000000000000000000000000000000000000001614610a5e5760405163041fb8cb60e31b815260040160405180910390fd5b80517f00000000000000000000000000000000000000000000000000000000000000006001600160a01b039081169116145f610a9b8360a0902090565b5f8181526001602052604081208054929350918190610100900460ff1615610af0578254610ae19087908790620100008104600290810b91600160281b9004900b61101c565b845461ff001916855590925090505b6001830180545f918290556002850182905590610b2d887f00000000000000000000000000000000000000000000000000000000000000006112bb565b90505f816001600160a01b03166361d027b36040518163ffffffff1660e01b8152600401602060405180830381865afa158015610b6c573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610b90919061233f565b90508215610c52576040516323b872dd60e01b81526001600160a01b037f0000000000000000000000000000000000000000000000000000000000000000811660048301528281166024830152604482018590527f000000000000000000000000000000000000000000000000000000000000000016906323b872dd906064016020604051808303815f875af1158015610c2c573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610c509190612324565b505b8415610cea5760405163a9059cbb60e01b81526001600160a01b038281166004830152602482018790527f0000000000000000000000000000000000000000000000000000000000000000169063a9059cbb906044016020604051808303815f875af1158015610cc4573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610ce89190612324565b505b8315610da65760405163a9059cbb60e01b81526001600160a01b0382811660048301526024820186905283169063a9059cbb906044016020604051808303815f875af1158015610d3c573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610d609190612324565b50604080516001600160a01b03831681526020810186905288917f6f25beea688da23574729528d9040ac00b2a9f98fe04601175b5bed75222d37b910160405180910390a25b867f98332f6bdb1b434256cc2c7b313581d76b7763b9c764bd32b25d461ff42c2bc382610dd38689612311565b604080516001600160a01b03909316835260208301919091520160405180910390a2505050505050505050565b610e2a827f00000000000000000000000000000000000000000000000000000000000000006112bb565b6001600160a01b03166302d05d3f6040518163ffffffff1660e01b8152600401602060405180830381865afa158015610e65573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610e89919061233f565b6001600160a01b0316336001600160a01b031614610eba57604051632a118c8960e01b815260040160405180910390fd5b5f60015f610ec98560a0902090565b815260208101919091526040015f20805490915060ff16151582151503610eef57505050565b8115610f6f576040516356a4eb3760e11b81526001600160a01b037f0000000000000000000000000000000000000000000000000000000000000000169063ad49d66e90610f4190869060040161239d565b5f604051808303815f87803b158015610f58575f5ffd5b505af1158015610f6a573d5f5f3e3d5ffd5b505050505b805460ff191682151517815560a0832060405183151581527f88e359a3e31b529597eae3a8c8a107e55d6ff85edf8ca19a7368a9be35f012719060200160405180910390a2505050565b610fc16112e7565b63389a75e1600c52805f526020600c208054421115610fe757636f5e88185f526004601cfd5b5f9055610ff381611301565b50565b610ffe6112e7565b8060601b61101357637448fbae5f526004601cfd5b610ff381611301565b5f5f5f61106b61102d8860a0902090565b6001600160a01b037f0000000000000000000000000000000000000000000000000000000000000000169030888866189a591dd85b1b60ca1b611347565b505090505f61108688878785611080906123ab565b306116f1565b9050866110a65761109781600f0b90565b6110a18260801d90565b6110ba565b6110b08160801d90565b6110ba82600f0b90565b6001600160801b039182169a911698509650505050505050565b5f5f5f5f5f6110e286611a1a565b604051631e2eaeaf60e01b8152600481018290529091505f906001600160a01b03891690631e2eaeaf90602401602060405180830381865afa15801561112a573d5f5f3e3d5ffd5b505050506040513d601f19601f8201168201806040525081019061114e91906123d8565b90506001600160a01b03811695508060a01c60020b945062ffffff8160b81c16935062ffffff8160d01c169250505092959194509250565b5f8361119c576111976001846123ef565b6111a7565b6111a7836001612414565b90505f5f5f86156111f1576111c0600285900b5f611a56565b92506111cd603c84612414565b91506111ea6111db8461139e565b6111e48461139e565b87611aec565b905061122d565b611200600285900b6001611a56565b915061120d603c836123ef565b925061122a61121b8461139e565b6112248461139e565b87611b5f565b90505b61125a888484847f00000000000000000000000000000000000000000000000000000000000000006116f1565b505f60015f61126a8b60a0902090565b815260208101919091526040015f20805467ffffffffffff000019166201000062ffffff9687160267ffffff0000000000191617600160281b94909516939093029390931790915550505050505050565b81515f906001600160a01b038084169116146112d85782516112de565b82602001515b90505b92915050565b638b78c6d81954331461088b576382b429005f526004601cfd5b638b78c6d81980546001600160a01b039092169182907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e05f80a3811560ff1b8217905550565b60408051602681018390526006810184905260038101859052858152603a600c8201205f92820183905260208201839052908290528190819061138b8a8a83611b9c565b919c909b50909950975050505050505050565b60020b5f60ff82901d80830118620d89e88111156113c7576113c76345c3193d60e11b84611c3f565b7001fffcb933bd6fad37aa2d162d1a5940016001821602600160801b186002821615611403576ffff97272373d413259a46990580e213a0260801c5b6004821615611422576ffff2e50f5f656932ef12357cf3c7fdcc0260801c5b6008821615611441576fffe5caca7e10e4e61c3624eaa0941cd00260801c5b6010821615611460576fffcb9843d60f6159c9db58835c9266440260801c5b602082161561147f576fff973b41fa98c081472e6896dfb254c00260801c5b604082161561149e576fff2ea16466c96a3843ec78b326b528610260801c5b60808216156114bd576ffe5dee046a99a2a811c461f1969c30530260801c5b6101008216156114dd576ffcbe86c7900a88aedcffc83b479aa3a40260801c5b6102008216156114fd576ff987a7253ac413176f2b074cf7815e540260801c5b61040082161561151d576ff3392b0822b70005940c7a398e4b70f30260801c5b61080082161561153d576fe7159475a2c29b7443b29c7fa6e889d90260801c5b61100082161561155d576fd097f3bdfd2022b8845ad8f792aa58250260801c5b61200082161561157d576fa9f746462d870fdf8a65dc1f90e061e50260801c5b61400082161561159d576f70d869a156d2a1b890bb3df62baf32f70260801c5b6180008216156115bd576f31be135f97d08fd981231505542fcfa60260801c5b620100008216156115de576f09aa508b5b7a84e1c677de54f3e99bc90260801c5b620200008216156115fe576e5d6af8dedb81196699c329225ee6040260801c5b6204000082161561161d576d2216e584f5fa1ea926041bedfe980260801c5b6208000082161561163a576b048a170391f7dc42444e8fa20260801c5b5f841315611646575f19045b63ffffffff0160201c9392505050565b5f5f836001600160a01b0316856001600160a01b03161115611676579293925b846001600160a01b0316866001600160a01b0316116116a15761169a858585611c4e565b91506116e8565b836001600160a01b0316866001600160a01b031610156116da576116c6868585611c4e565b91506116d3858785611cc0565b90506116e8565b6116e5858585611cc0565b90505b94509492505050565b5f7f00000000000000000000000000000000000000000000000000000000000000006001600160a01b0316635a6bcfda8760405180608001604052808960020b81526020018860020b815260200187600f0b815260200166189a591dd85b1b60ca1b8152506040518363ffffffff1660e01b8152600401611773929190612439565b60408051808303815f875af115801561178e573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906117b2919061248a565b5090505f6117c08260801d90565b600f0b12156118235761181e7f0000000000000000000000000000000000000000000000000000000000000000836117f88460801d90565b611801906123ab565b89516001600160a01b03169291906001600160801b03165f611d09565b6118e1565b5f61182e8260801d90565b600f0b13156118e1577f00000000000000000000000000000000000000000000000000000000000000006001600160a01b0316630b0d9c09875f0151846118758560801d90565b6040516001600160e01b031960e086901b1681526001600160a01b0393841660048201529290911660248301526001600160801b031660448201526064015f604051808303815f87803b1580156118ca575f5ffd5b505af11580156118dc573d5f5f3e3d5ffd5b505050505b5f6118ec82600f0b90565b600f0b12156119525761194d7f00000000000000000000000000000000000000000000000000000000000000008361192484600f0b90565b61192d906123ab565b60208a01516001600160a01b03169291906001600160801b03165f611d09565b611a11565b5f61195d82600f0b90565b600f0b1315611a11577f00000000000000000000000000000000000000000000000000000000000000006001600160a01b0316630b0d9c098760200151846119a585600f0b90565b6040516001600160e01b031960e086901b1681526001600160a01b0393841660048201529290911660248301526001600160801b031660448201526064015f604051808303815f87803b1580156119fa575f5ffd5b505af1158015611a0c573d5f5f3e3d5ffd5b505050505b95945050505050565b6040515f90611a39908390600690602001918252602082015260400190565b604051602081830303815290604052805190602001209050919050565b5f620d89b319600284900b1215611a7357620d89b3199250611a89565b620d89b4600284900b1315611a8957620d89b492505b611a94603c846124c0565b60020b5f03611aa45750816112e1565b603c611ab081856124e1565b611aba9190612519565b90505f8360020b1215611ad557611ad2603c826123ef565b90505b816112e157611ae5603c82612414565b90506112e1565b5f826001600160a01b0316846001600160a01b03161115611b0b579192915b5f611b2d856001600160a01b0316856001600160a01b0316600160601b611fd4565b9050611b54611b4f8483611b41898961253f565b6001600160a01b0316611fd4565b612070565b9150505b9392505050565b5f826001600160a01b0316846001600160a01b03161115611b7e579192915b611b94611b4f83600160601b611b41888861253f565b949350505050565b5f5f5f5f611baa86866120c7565b604051631afeb18d60e11b815260048101829052600360248201529091505f906001600160a01b038916906335fd631a906044015f60405180830381865afa158015611bf8573d5f5f3e3d5ffd5b505050506040513d5f823e601f3d908101601f19168201604052611c1f919081019061255e565b60208101516040820151606090920151909a919950975095505050505050565b815f528060020b60045260245ffd5b5f826001600160a01b0316846001600160a01b03161115611c6d579192915b6001600160a01b038416611cb66fffffffffffffffffffffffffffffffff60601b606085901b16611c9e878761253f565b6001600160a01b0316866001600160a01b0316611fd4565b611b94919061260a565b5f826001600160a01b0316846001600160a01b03161115611cdf579192915b611b946001600160801b038316611cf6868661253f565b6001600160a01b0316600160601b611fd4565b8015611d9d57836001600160a01b031663f5298aca84611d38886001600160a01b03166001600160a01b031690565b6040516001600160e01b031960e085901b1681526001600160a01b0390921660048301526024820152604481018590526064015f604051808303815f87803b158015611d82575f5ffd5b505af1158015611d94573d5f5f3e3d5ffd5b50505050611fcd565b6001600160a01b038516611e1457836001600160a01b03166311da60b4836040518263ffffffff1660e01b815260040160206040518083038185885af1158015611de9573d5f5f3e3d5ffd5b50505050506040513d601f19601f82011682018060405250810190611e0e91906123d8565b50611fcd565b604051632961046560e21b81526001600160a01b03868116600483015285169063a5841194906024015f604051808303815f87803b158015611e54575f5ffd5b505af1158015611e66573d5f5f3e3d5ffd5b505050506001600160a01b0383163014611ef8576040516323b872dd60e01b81526001600160a01b0384811660048301528581166024830152604482018490528616906323b872dd906064016020604051808303815f875af1158015611ece573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190611ef29190612324565b50611f6a565b60405163a9059cbb60e01b81526001600160a01b0385811660048301526024820184905286169063a9059cbb906044016020604051808303815f875af1158015611f44573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190611f689190612324565b505b836001600160a01b03166311da60b46040518163ffffffff1660e01b81526004016020604051808303815f875af1158015611fa7573d5f5f3e3d5ffd5b505050506040513d601f19601f82011682018060405250810190611fcb91906123d8565b505b5050505050565b5f838302815f1985870982811083820303915050808411611ff3575f5ffd5b805f0361200557508290049050611b58565b5f848688095f868103871696879004966002600389028118808a02820302808a02820302808a02820302808a02820302808a02820302808a02909103029181900381900460010186841190950394909402919094039290920491909117919091029150509392505050565b806001600160801b03811681146120c25760405162461bcd60e51b81526020600482015260126024820152716c6971756964697479206f766572666c6f7760701b604482015260640160405180910390fd5b919050565b5f5f6120d284611a1a565b90505f6120e0600683612311565b6040805160208101879052908101829052909150606001604051602081830303815290604052805190602001209250505092915050565b634e487b7160e01b5f52604160045260245ffd5b604051601f8201601f1916810167ffffffffffffffff8111828210171561215457612154612117565b604052919050565b6001600160a01b0381168114610ff3575f5ffd5b8035600281900b81146120c2575f5ffd5b5f60a08284031215612191575f5ffd5b60405160a0810167ffffffffffffffff811182821017156121b4576121b4612117565b60405290508082356121c58161215c565b815260208301356121d58161215c565b6020820152604083013562ffffff811681146121ef575f5ffd5b604082015261220060608401612170565b606082015260808301356122138161215c565b6080919091015292915050565b8015158114610ff3575f5ffd5b5f5f5f5f6101008587031215612241575f5ffd5b61224b8686612181565b935060a0850135925061226060c08601612170565b915060e085013561227081612220565b939692955090935050565b5f6020828403121561228b575f5ffd5b5035919050565b5f60a082840312156122a2575f5ffd5b6112de8383612181565b5f5f60c083850312156122bd575f5ffd5b6122c78484612181565b915060a08301356122d781612220565b809150509250929050565b5f602082840312156122f2575f5ffd5b8135611b588161215c565b634e487b7160e01b5f52601160045260245ffd5b808201808211156112e1576112e16122fd565b5f60208284031215612334575f5ffd5b8151611b5881612220565b5f6020828403121561234f575f5ffd5b8151611b588161215c565b80516001600160a01b03908116835260208083015182169084015260408083015162ffffff169084015260608083015160020b9084015260809182015116910152565b60a081016112e1828461235a565b5f81600f0b6f7fffffffffffffffffffffffffffffff1981036123d0576123d06122fd565b5f0392915050565b5f602082840312156123e8575f5ffd5b5051919050565b600282810b9082900b03627fffff198112627fffff821317156112e1576112e16122fd565b600281810b9083900b01627fffff8113627fffff19821217156112e1576112e16122fd565b612443818461235a565b8151600290810b60a08301526020830151900b60c0820152604082015160e082015260609091015161010082015261014061012082018190525f9082015261016001919050565b5f5f6040838503121561249b575f5ffd5b505080516020909101519092909150565b634e487b7160e01b5f52601260045260245ffd5b5f8260020b806124d2576124d26124ac565b808360020b0791505092915050565b5f8160020b8360020b806124f7576124f76124ac565b627fffff1982145f1982141615612510576125106122fd565b90059392505050565b5f8260020b8260020b028060020b9150808214612538576125386122fd565b5092915050565b6001600160a01b0382811682821603908111156112e1576112e16122fd565b5f6020828403121561256e575f5ffd5b815167ffffffffffffffff811115612584575f5ffd5b8201601f81018413612594575f5ffd5b805167ffffffffffffffff8111156125ae576125ae612117565b8060051b6125be6020820161212b565b918252602081840181019290810190878411156125d9575f5ffd5b6020850194505b838510156125ff578451808352602095860195909350909101906125e0565b979650505050505050565b5f82612618576126186124ac565b50049056fea26469706673582212202b032cc4115d2ebc13f25c45e9ab739c415fdbbd2de805f5d4ff3493569e954364736f6c634300081c0033"

    @overload
    @classmethod
    def deploy(cls, _initialSqrtPriceX96: uint160, _protocolOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#65)

        Args:
            _initialSqrtPriceX96: uint160
            _protocolOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _initialSqrtPriceX96: uint160, _protocolOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> FlayHooks:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#65)

        Args:
            _initialSqrtPriceX96: uint160
            _protocolOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _initialSqrtPriceX96: uint160, _protocolOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#65)

        Args:
            _initialSqrtPriceX96: uint160
            _protocolOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _initialSqrtPriceX96: uint160, _protocolOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#65)

        Args:
            _initialSqrtPriceX96: uint160
            _protocolOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _initialSqrtPriceX96: uint160, _protocolOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[FlayHooks]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#65)

        Args:
            _initialSqrtPriceX96: uint160
            _protocolOwner: address
        """
        ...

    @classmethod
    def deploy(cls, _initialSqrtPriceX96: uint160, _protocolOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, FlayHooks, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[FlayHooks]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#65)

        Args:
            _initialSqrtPriceX96: uint160
            _protocolOwner: address
        """
        return cls._deploy(request_type, [_initialSqrtPriceX96, _protocolOwner], return_tx, FlayHooks, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class CannotBeInitializedDirectly(TransactionRevertedError):
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#32)
        """
        _abi = {'inputs': [], 'name': 'CannotBeInitializedDirectly', 'type': 'error'}
        original_name = 'CannotBeInitializedDirectly'
        selector = bytes4(b'\xa2-a\xd6')



    @overload
    def nativeToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#35)

        Returns:
            nativeToken: address
        """
        ...

    @overload
    def nativeToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#35)

        Returns:
            nativeToken: address
        """
        ...

    @overload
    def nativeToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#35)

        Returns:
            nativeToken: address
        """
        ...

    @overload
    def nativeToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#35)

        Returns:
            nativeToken: address
        """
        ...

    def nativeToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#35)

        Returns:
            nativeToken: address
        """
        return self._execute(self.chain, request_type, "e1758bd8", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def flayToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#36)

        Returns:
            flayToken: address
        """
        ...

    @overload
    def flayToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#36)

        Returns:
            flayToken: address
        """
        ...

    @overload
    def flayToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#36)

        Returns:
            flayToken: address
        """
        ...

    @overload
    def flayToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#36)

        Returns:
            flayToken: address
        """
        ...

    def flayToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#36)

        Returns:
            flayToken: address
        """
        return self._execute(self.chain, request_type, "19cca5c6", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def _poolManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#39)

        Returns:
            _poolManager: address
        """
        ...

    @overload
    def _poolManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#39)

        Returns:
            _poolManager: address
        """
        ...

    @overload
    def _poolManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#39)

        Returns:
            _poolManager: address
        """
        ...

    @overload
    def _poolManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#39)

        Returns:
            _poolManager: address
        """
        ...

    def _poolManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#39)

        Returns:
            _poolManager: address
        """
        return self._execute(self.chain, request_type, "aace008e", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def BASE_SWAP_FEE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint24:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#45)

        Returns:
            BASE_SWAP_FEE: uint24
        """
        ...

    @overload
    def BASE_SWAP_FEE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#45)

        Returns:
            BASE_SWAP_FEE: uint24
        """
        ...

    @overload
    def BASE_SWAP_FEE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#45)

        Returns:
            BASE_SWAP_FEE: uint24
        """
        ...

    @overload
    def BASE_SWAP_FEE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint24]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#45)

        Returns:
            BASE_SWAP_FEE: uint24
        """
        ...

    def BASE_SWAP_FEE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint24, TransactionAbc[uint24], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#45)

        Returns:
            BASE_SWAP_FEE: uint24
        """
        return self._execute(self.chain, request_type, "12a5d5bf", [], True if request_type == "tx" else False, uint24, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def MIN_DISTRIBUTE_THRESHOLD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#48)

        Returns:
            MIN_DISTRIBUTE_THRESHOLD: uint256
        """
        ...

    @overload
    def MIN_DISTRIBUTE_THRESHOLD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#48)

        Returns:
            MIN_DISTRIBUTE_THRESHOLD: uint256
        """
        ...

    @overload
    def MIN_DISTRIBUTE_THRESHOLD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#48)

        Returns:
            MIN_DISTRIBUTE_THRESHOLD: uint256
        """
        ...

    @overload
    def MIN_DISTRIBUTE_THRESHOLD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#48)

        Returns:
            MIN_DISTRIBUTE_THRESHOLD: uint256
        """
        ...

    def MIN_DISTRIBUTE_THRESHOLD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#48)

        Returns:
            MIN_DISTRIBUTE_THRESHOLD: uint256
        """
        return self._execute(self.chain, request_type, "299d532e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def bidWall(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> BidWall:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#51)

        Returns:
            bidWall: contract BidWall
        """
        ...

    @overload
    def bidWall(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#51)

        Returns:
            bidWall: contract BidWall
        """
        ...

    @overload
    def bidWall(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#51)

        Returns:
            bidWall: contract BidWall
        """
        ...

    @overload
    def bidWall(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[BidWall]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#51)

        Returns:
            bidWall: contract BidWall
        """
        ...

    def bidWall(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[BidWall, TransactionAbc[BidWall], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#51)

        Returns:
            bidWall: contract BidWall
        """
        return self._execute(self.chain, request_type, "ba3e69b7", [], True if request_type == "tx" else False, BidWall, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def flayNativePoolKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> PoolKey:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#54)

        Returns:
            flayNativePoolKey: struct PoolKey
        """
        ...

    @overload
    def flayNativePoolKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#54)

        Returns:
            flayNativePoolKey: struct PoolKey
        """
        ...

    @overload
    def flayNativePoolKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#54)

        Returns:
            flayNativePoolKey: struct PoolKey
        """
        ...

    @overload
    def flayNativePoolKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[PoolKey]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#54)

        Returns:
            flayNativePoolKey: struct PoolKey
        """
        ...

    def flayNativePoolKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[PoolKey, TransactionAbc[PoolKey], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#54)

        Returns:
            flayNativePoolKey: struct PoolKey
        """
        return self._execute(self.chain, request_type, "3c371096", [], True if request_type == "tx" else False, PoolKey, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getHookPermissions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Hooks.Permissions:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#92)

        Returns:
            struct Hooks.Permissions
        """
        ...

    @overload
    def getHookPermissions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#92)

        Returns:
            struct Hooks.Permissions
        """
        ...

    @overload
    def getHookPermissions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#92)

        Returns:
            struct Hooks.Permissions
        """
        ...

    @overload
    def getHookPermissions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Hooks.Permissions]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#92)

        Returns:
            struct Hooks.Permissions
        """
        ...

    def getHookPermissions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Hooks.Permissions, TransactionAbc[Hooks.Permissions], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#92)

        Returns:
            struct Hooks.Permissions
        """
        return self._execute(self.chain, request_type, "c4e833ce", [], True if request_type == "tx" else False, Hooks.Permissions, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def beforeInitialize(self, arg1: Union[Account, Address], arg2: PoolKey, arg3: uint160, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#118)

        Args:
            arg1: address
            arg2: struct PoolKey
            arg3: uint160
        Returns:
            bytes4
        """
        ...

    @overload
    def beforeInitialize(self, arg1: Union[Account, Address], arg2: PoolKey, arg3: uint160, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#118)

        Args:
            arg1: address
            arg2: struct PoolKey
            arg3: uint160
        Returns:
            bytes4
        """
        ...

    @overload
    def beforeInitialize(self, arg1: Union[Account, Address], arg2: PoolKey, arg3: uint160, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#118)

        Args:
            arg1: address
            arg2: struct PoolKey
            arg3: uint160
        Returns:
            bytes4
        """
        ...

    @overload
    def beforeInitialize(self, arg1: Union[Account, Address], arg2: PoolKey, arg3: uint160, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#118)

        Args:
            arg1: address
            arg2: struct PoolKey
            arg3: uint160
        Returns:
            bytes4
        """
        ...

    def beforeInitialize(self, arg1: Union[Account, Address], arg2: PoolKey, arg3: uint160, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#118)

        Args:
            arg1: address
            arg2: struct PoolKey
            arg3: uint160
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "dc98354e", [arg1, arg2, arg3], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def beforeSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bytes4, int256, uint24]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#138)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            arg2: bytes
        Returns:
            selector_: bytes4
            beforeSwapDelta_: BeforeSwapDelta
            uint24
        """
        ...

    @overload
    def beforeSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#138)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            arg2: bytes
        Returns:
            selector_: bytes4
            beforeSwapDelta_: BeforeSwapDelta
            uint24
        """
        ...

    @overload
    def beforeSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#138)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            arg2: bytes
        Returns:
            selector_: bytes4
            beforeSwapDelta_: BeforeSwapDelta
            uint24
        """
        ...

    @overload
    def beforeSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bytes4, int256, uint24]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#138)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            arg2: bytes
        Returns:
            selector_: bytes4
            beforeSwapDelta_: BeforeSwapDelta
            uint24
        """
        ...

    def beforeSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bytes4, int256, uint24], TransactionAbc[Tuple[bytes4, int256, uint24]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#138)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            arg2: bytes
        Returns:
            selector_: bytes4
            beforeSwapDelta_: BeforeSwapDelta
            uint24
        """
        return self._execute(self.chain, request_type, "575e24b4", [arg1, _key, _params, arg2], True if request_type == "tx" else False, Tuple[bytes4, int256, uint24], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def afterSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, _delta: int256, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bytes4, int128]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#186)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            _delta: BalanceDelta
            arg2: bytes
        Returns:
            selector_: bytes4
            hookDeltaUnspecified_: int128
        """
        ...

    @overload
    def afterSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, _delta: int256, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#186)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            _delta: BalanceDelta
            arg2: bytes
        Returns:
            selector_: bytes4
            hookDeltaUnspecified_: int128
        """
        ...

    @overload
    def afterSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, _delta: int256, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#186)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            _delta: BalanceDelta
            arg2: bytes
        Returns:
            selector_: bytes4
            hookDeltaUnspecified_: int128
        """
        ...

    @overload
    def afterSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, _delta: int256, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bytes4, int128]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#186)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            _delta: BalanceDelta
            arg2: bytes
        Returns:
            selector_: bytes4
            hookDeltaUnspecified_: int128
        """
        ...

    def afterSwap(self, arg1: Union[Account, Address], _key: PoolKey, _params: IPoolManager.SwapParams, _delta: int256, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bytes4, int128], TransactionAbc[Tuple[bytes4, int128]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///C:/Users/user/Downloads/flaunchgg-contracts/src/contracts/FlayHooks.sol#186)

        Args:
            arg1: address
            _key: struct PoolKey
            _params: struct IPoolManager.SwapParams
            _delta: BalanceDelta
            arg2: bytes
        Returns:
            selector_: bytes4
            hookDeltaUnspecified_: int128
        """
        return self._execute(self.chain, request_type, "b47b2fb1", [arg1, _key, _params, _delta, arg2], True if request_type == "tx" else False, Tuple[bytes4, int128], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

FlayHooks.nativeToken.selector = bytes4(b'\xe1u\x8b\xd8')
FlayHooks.flayToken.selector = bytes4(b'\x19\xcc\xa5\xc6')
FlayHooks._poolManager.selector = bytes4(b'\xaa\xce\x00\x8e')
FlayHooks.BASE_SWAP_FEE.selector = bytes4(b'\x12\xa5\xd5\xbf')
FlayHooks.MIN_DISTRIBUTE_THRESHOLD.selector = bytes4(b')\x9dS.')
FlayHooks.bidWall.selector = bytes4(b'\xba>i\xb7')
FlayHooks.flayNativePoolKey.selector = bytes4(b'<7\x10\x96')
FlayHooks.getHookPermissions.selector = bytes4(b'\xc4\xe83\xce')
FlayHooks.beforeInitialize.selector = bytes4(b'\xdc\x985N')
FlayHooks.beforeSwap.selector = bytes4(b'W^$\xb4')
FlayHooks.afterSwap.selector = bytes4(b'\xb4{/\xb1')
