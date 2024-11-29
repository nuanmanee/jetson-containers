from jetson_containers import CUDA_ARCHITECTURES

def AutoAWQ(version, kernels_version, default=False):
    pkg = package.copy()

    pkg['name'] = f'auto_awq:{version}'
    pkg['build_args'] = {
        'AUTOAWQ_VERSION': version,
        'AUTOAWQ_KERNELS_VERSION': kernels_version,
        'COMPUTE_CAPABILITIES': ','.join([str(x) for x in CUDA_ARCHITECTURES]),
    }

    builder = pkg.copy()
    
    builder['name'] = f'auto_awq:{version}-builder'
    builder['build_args'] = {**pkg['build_args'], **{'FORCE_BUILD': 'on'}}

    if default:
        pkg['alias'] = 'auto_awq'
        builder['alias'] = 'auto_awq:builder'
    
    return pkg, builder

package = [
    AutoAWQ('0.2.7.post2', '0.0.9', default=False),
    AutoAWQ('0.2.6', '0.0.8', default=True),
    AutoAWQ('0.2.4', '0.0.6', default=False),
]
