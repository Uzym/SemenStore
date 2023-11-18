'use client'

import { IconButton, Typography } from '@mui/material'
import CartIcon from '../ui/СartIcon/CartIcon'
import classNames from 'classnames'
import { montserrat } from '@/theme/fonts'
import CartPage from '../pages/CartPage/CartPage'
import { useState } from 'react'
import styles from './MainLayout.module.scss'
import Link from 'next/link'

const MainLayout = () => {
	const [isCartOpen, setIsCartOpen] = useState(false)

	return (
		<>
			<header className={styles.header}>
				<Link href={'/'}>
					<Typography
						className={classNames(styles.title, montserrat.className)}
					>
						UStore
					</Typography>
				</Link>
				<IconButton
					className={classNames(styles.icon, {
						['bg-ns-black hover:bg-ns-black']: isCartOpen,
					})}
					sx={{
						'& .MuiTouchRipple-root .MuiTouchRipple-child': {
							borderRadius: '7px',
						},
					}}
					onClick={() => setIsCartOpen(!isCartOpen)}
				>
					{isCartOpen ? <CartIcon color='#FFFFFF' /> : <CartIcon />}
				</IconButton>
			</header>
			<CartPage isCartOpen={isCartOpen} setIsCartOpen={setIsCartOpen} />
		</>
	)
}

export default MainLayout
