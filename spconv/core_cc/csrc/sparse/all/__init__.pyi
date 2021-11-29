from typing import overload, Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union
from pccm.stubs import EnumValue, EnumClassValue
from cumm.tensorview import Tensor
class ThrustCustomAllocatorV2:
    alloc_func: Callable[int, int]
class SpconvOps:
    @staticmethod
    def cumm_version() -> str: 
        """
        get cumm version when build spconv.
                
        """
        ...
    @staticmethod
    def pccm_version() -> str: 
        """
        get pccm version when build spconv.
                
        """
        ...
    @staticmethod
    def generate_conv_inds_stage1(indices: Tensor, indice_pairs: Tensor, indice_pairs_uniq: Tensor, indice_num_per_loc: Tensor, batch_size: int, output_dims: List[int], input_dims: List[int], ksize: List[int], stride: List[int], padding: List[int], dilation: List[int], transposed: bool = False, stream_int: int = 0) -> None: 
        """
        Args:
            indices: 
            indice_pairs: 
            indice_pairs_uniq: 
            indice_num_per_loc: 
            batch_size: 
            output_dims: 
            input_dims: 
            ksize: 
            stride: 
            padding: 
            dilation: 
            transposed: 
            stream_int: 
        """
        ...
    @staticmethod
    def generate_conv_inds_stage1_5(indice_pairs_uniq: Tensor, ndim: int, uniq_size: int, stream_int: int = 0) -> int: 
        """
        Args:
            indice_pairs_uniq: 
            ndim: 
            uniq_size: 
            stream_int: 
        """
        ...
    @staticmethod
    def generate_conv_inds_stage2(indices: Tensor, hashdata: Tensor, indice_pairs: Tensor, indice_pairs_uniq: Tensor, out_inds: Tensor, num_out_act: int, batch_size: int, output_dims: List[int], input_dims: List[int], ksize: List[int], stride: List[int], padding: List[int], dilation: List[int], transposed: bool = False, stream_int: int = 0) -> int: 
        """
        Args:
            indices: 
            hashdata: 
            indice_pairs: 
            indice_pairs_uniq: 
            out_inds: 
            num_out_act: 
            batch_size: 
            output_dims: 
            input_dims: 
            ksize: 
            stride: 
            padding: 
            dilation: 
            transposed: 
            stream_int: 
        """
        ...
    @staticmethod
    def generate_conv_inds_mask_stage1(indices: Tensor, indice_pairs_bwd: Tensor, indice_pairs_uniq: Tensor, indice_num_per_loc: Tensor, batch_size: int, output_dims: List[int], input_dims: List[int], ksize: List[int], stride: List[int], padding: List[int], dilation: List[int], transposed: bool = False, stream_int: int = 0) -> None: 
        """
        Args:
            indices: 
            indice_pairs_bwd: 
            indice_pairs_uniq: 
            indice_num_per_loc: 
            batch_size: 
            output_dims: 
            input_dims: 
            ksize: 
            stride: 
            padding: 
            dilation: 
            transposed: 
            stream_int: 
        """
        ...
    @staticmethod
    def generate_conv_inds_mask_stage2(indices: Tensor, hashdata: Tensor, indice_pairs_fwd: Tensor, indice_pairs_bwd: Tensor, indice_pairs_uniq: Tensor, out_inds: Tensor, mask_fwd: Tensor, mask_bwd: Tensor, num_out_act: int, batch_size: int, output_dims: List[int], input_dims: List[int], ksize: List[int], stride: List[int], padding: List[int], dilation: List[int], transposed: bool = False, stream_int: int = 0) -> int: 
        """
        Args:
            indices: 
            hashdata: 
            indice_pairs_fwd: 
            indice_pairs_bwd: 
            indice_pairs_uniq: 
            out_inds: 
            mask_fwd: 
            mask_bwd: 
            num_out_act: 
            batch_size: 
            output_dims: 
            input_dims: 
            ksize: 
            stride: 
            padding: 
            dilation: 
            transposed: 
            stream_int: 
        """
        ...
    @staticmethod
    def generate_subm_conv_inds(indices: Tensor, hashdata: Tensor, indice_pairs: Tensor, out_inds: Tensor, indice_num_per_loc: Tensor, batch_size: int, input_dims: List[int], ksize: List[int], dilation: List[int], indice_pair_mask: Tensor =  Tensor(), backward: bool = False, stream_int: int =  0) -> int: 
        """
        Args:
            indices: 
            hashdata: 
            indice_pairs: 
            out_inds: 
            indice_num_per_loc: 
            batch_size: 
            input_dims: 
            ksize: 
            dilation: 
            indice_pair_mask: 
            backward: 
            stream_int: 
        """
        ...
    @staticmethod
    def generate_conv_inds_cpu(indices: Tensor, indice_pairs: Tensor, out_inds: Tensor, indice_num_per_loc: Tensor, batch_size: int, output_dims: List[int], input_dims: List[int], ksize: List[int], stride: List[int], padding: List[int], dilation: List[int], transposed: bool = False) -> int: 
        """
        Args:
            indices: 
            indice_pairs: 
            out_inds: 
            indice_num_per_loc: 
            batch_size: 
            output_dims: 
            input_dims: 
            ksize: 
            stride: 
            padding: 
            dilation: 
            transposed: 
        """
        ...
    @staticmethod
    def generate_subm_conv_inds_cpu(indices: Tensor, indice_pairs: Tensor, out_inds: Tensor, indice_num_per_loc: Tensor, batch_size: int, input_dims: List[int], ksize: List[int], dilation: List[int]) -> int: 
        """
        Args:
            indices: 
            indice_pairs: 
            out_inds: 
            indice_num_per_loc: 
            batch_size: 
            input_dims: 
            ksize: 
            dilation: 
        """
        ...
    @staticmethod
    def maxpool_forward(out: Tensor, inp: Tensor, out_inds: Tensor, in_inds: Tensor, stream: int = 0) -> None: 
        """
        Args:
            out: 
            inp: 
            out_inds: 
            in_inds: 
            stream: 
        """
        ...
    @staticmethod
    def maxpool_backward(out: Tensor, inp: Tensor, dout: Tensor, dinp: Tensor, out_inds: Tensor, in_inds: Tensor, stream: int = 0) -> None: 
        """
        Args:
            out: 
            inp: 
            dout: 
            dinp: 
            out_inds: 
            in_inds: 
            stream: 
        """
        ...
    @staticmethod
    def maxpool_implicit_gemm_forward(out: Tensor, inp: Tensor, inds: Tensor, stream: int = 0) -> None: 
        """
        Args:
            out: 
            inp: 
            inds: 
            stream: 
        """
        ...
    @staticmethod
    def maxpool_implicit_gemm_backward(out: Tensor, inp: Tensor, dout: Tensor, dinp: Tensor, inds: Tensor, stream: int = 0) -> None: 
        """
        Args:
            out: 
            inp: 
            dout: 
            dinp: 
            inds: 
            stream: 
        """
        ...
    @staticmethod
    def maxpool_forward_cpu(out: Tensor, inp: Tensor, out_inds: Tensor, in_inds: Tensor) -> None: 
        """
        Args:
            out: 
            inp: 
            out_inds: 
            in_inds: 
        """
        ...
    @staticmethod
    def maxpool_backward_cpu(out: Tensor, inp: Tensor, dout: Tensor, dinp: Tensor, out_inds: Tensor, in_inds: Tensor) -> None: 
        """
        Args:
            out: 
            inp: 
            dout: 
            dinp: 
            out_inds: 
            in_inds: 
        """
        ...
    @staticmethod
    def gather_cpu(out: Tensor, inp: Tensor, inds: Tensor) -> None: 
        """
        Args:
            out: 
            inp: 
            inds: 
        """
        ...
    @staticmethod
    def scatter_add_cpu(out: Tensor, inp: Tensor, inds: Tensor) -> None: 
        """
        Args:
            out: 
            inp: 
            inds: 
        """
        ...
    @staticmethod
    def sort_1d_by_key(data: Tensor, indices: Tensor =  Tensor(), stream: int = 0) -> Tensor: 
        """
        Args:
            data: 
            indices: 
            stream: 
        """
        ...
    @staticmethod
    def sort_1d_by_key_allocator(data: Tensor, alloc_func, indices: Tensor =  Tensor(), stream: int = 0) -> Tensor: 
        """
        Args:
            data: 
            alloc_func: 
            indices: 
            stream: 
        """
        ...
    @staticmethod
    def sort_1d_by_key_split(data: Tensor, mask: Tensor, indices: Tensor =  Tensor(), stream: int = 0, mask_output: bool = False) -> Tensor: 
        """
        Args:
            data: 
            mask: 
            indices: 
            stream: 
            mask_output: 
        """
        ...
    @staticmethod
    def sort_1d_by_key_split_allocator(data: Tensor, alloc_func, mask: Tensor, indices: Tensor =  Tensor(), stream: int = 0, mask_output: bool = False) -> Tensor: 
        """
        Args:
            data: 
            alloc_func: 
            mask: 
            indices: 
            stream: 
            mask_output: 
        """
        ...
    @staticmethod
    def count_bits(a: Tensor) -> Tensor: 
        """
        Args:
            a: 
        """
        ...
    @staticmethod
    def reverse_bits(a: Tensor) -> Tensor: 
        """
        Args:
            a: 
        """
        ...
    @staticmethod
    def calc_point2voxel_meta_data(vsize_xyz: List[float], coors_range_xyz: List[float]) -> Tuple[List[float], List[int], List[int], List[float]]: 
        """
        Args:
            vsize_xyz: 
            coors_range_xyz: 
        """
        ...
    @staticmethod
    def point2voxel_cpu(points: Tensor, voxels: Tensor, indices: Tensor, num_per_voxel: Tensor, densehashdata: Tensor, pc_voxel_id: Tensor, vsize: List[float], grid_size: List[int], grid_stride: List[int], coors_range: List[float], empty_mean: bool = False, clear_voxels: bool = True) -> Tuple[Tensor, Tensor, Tensor]: 
        """
        Args:
            points: 
            voxels: 
            indices: 
            num_per_voxel: 
            densehashdata: 
            pc_voxel_id: 
            vsize: 
            grid_size: 
            grid_stride: 
            coors_range: 
            empty_mean: 
            clear_voxels: 
        """
        ...
    @staticmethod
    def point2voxel_cuda(points: Tensor, voxels: Tensor, indices: Tensor, num_per_voxel: Tensor, hashdata: Tensor, point_indice_data: Tensor, pc_voxel_id: Tensor, vsize: List[float], grid_size: List[int], grid_stride: List[int], coors_range: List[float], empty_mean: bool = False, clear_voxels: bool = True, stream_int: int = 0) -> Tuple[Tensor, Tensor, Tensor]: 
        """
        Args:
            points: 
            voxels: 
            indices: 
            num_per_voxel: 
            hashdata: 
            point_indice_data: 
            pc_voxel_id: 
            vsize: 
            grid_size: 
            grid_stride: 
            coors_range: 
            empty_mean: 
            clear_voxels: 
            stream_int: 
        """
        ...
